#!/usr/bin/python3

plainText = input("Insert your ciphertext: ")
shift = int(input("Enter your shift: "))


def caesar(plainText, shift):
    cipherText = ""
    for ch in plainText:
        if ch.isdigit():
            stayInAlphabet = ord(ch) - shift
            while stayInAlphabet < ord('0'):
                stayInAlphabet += 10
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
        if ch.isalpha():
            stayInAlphabet = ord(ch) - shift
            while stayInAlphabet < ord('a'):
                stayInAlphabet += 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
    print ("Your ciphertext is: ", cipherText)
    return cipherText


caesar(plainText, shift)
