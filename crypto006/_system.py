import random
import SocketServer
import threading
import time
import string
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.PublicKey import RSA


def gcd(u, v):
    return gcd(v, u % v) if v else abs(u)


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


def crt(n, a):
    lena = len(n)
    p = i = prod = 1;
    sm = 0
    for i in range(lena): prod *= n[i]
    for i in range(lena):
        p = prod / n[i]
        sm += a[i] * modinv(p, n[i]) * p
    return sm % prod


def randchar(l):
    s = ''
    num = len(string.printable)
    random.seed()
    for i in range(l):
        s += string.printable[random.randint(0, num - 1)]
    return s


def hardware_error(m):
    probability = 0.01
    sx = random.random()
    if sx <= probability:
        k = bytearray(bin(m))
        i = random.randint(2, len(k))
        if k[i] == ord('1'):
            k[i] = ord('0')
        else:
            k[i] = ord('1')
        m = int(str(k), 2)
    return m


def read_key():
    key = RSA.importKey(open('private.pem').read())
    dp = key.d % (key.p - 1)
    dq = key.d % (key.q - 1)
    return key.n, key.e, key.d, key.p, key.q, dp, dq


def my_pow(a, b, c):
    return pow(a, hardware_error(b), c)


def calculate_signature(m):
    num = bytes_to_long(m)
    mp = num % p
    mq = num % q
    sp = my_pow(mp, dp, p)
    sq = my_pow(mq, dq, q)
    t1 = crt([p, q], [1, 0])
    t2 = crt([p, q], [0, 1])
    return long_to_bytes((t1 * sp + t2 * sq) % n)


def verify_signature(m, sig):
    return pow(bytes_to_long(sig), e, n) == bytes_to_long(m)


(n, e, d, p, q, dp, dq) = read_key()

flag = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


class Incoming(SocketServer.BaseRequestHandler):
    def handle(self):
        cur_thread = threading.current_thread()
        welcome = """
*******************************************
*** Welcome to RSA Signature System! ***
"""
        self.request.send(welcome)
        for i in xrange(20):
            time.sleep(0.2)
            self.request.send(".")

        while True:

            self.request.send("\n1. Test system")
            self.request.send("\n2. Try break system")
            self.request.send("\n3. Exit")
            self.request.send("\nYour choice:")
            try:
                choice = int(self.request.recv(1024).strip("\n"))
            except:
                self.request.send('You must choice [1-3].')
                continue
            if choice == 1:
                self.request.send("\nEnter a message you wish to calculate signature: ")
                m = self.request.recv(1024).strip("\n")
                self.request.send("Your signature is:\n")
                self.request.send("==================================\n")
                self.request.send(calculate_signature(m).encode("hex"))
                self.request.send("\n==================================\n")
            elif choice == 2:
                m = randchar(100)
                self.request.send("\nIf you can calculate signature of my message, I will give you flag.")
                self.request.send("\nMy message: %s" % m.encode('hex'))
                self.request.send("\nInput your signature: ")
                try:
                    sig = self.request.recv(1024).strip("\n")
                    sig = sig.decode('hex')
                except:
                    self.request.send("Sorry, wrong signature format.\n")
                    continue
                if verify_signature(m, sig):
                    self.request.send("Good job, flag: %s" % flag)
                else:
                    self.request.send("Sorry, not verified @.\n")
            elif choice == 3:
                self.request.send("\nGood bye.")
                break
            else:
                self.request.send('You are kidding me huh @@.\n')


server = ThreadedServer(("0.0.0.0", 6000), Incoming)
server.timeout = 4
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

server_thread.join()