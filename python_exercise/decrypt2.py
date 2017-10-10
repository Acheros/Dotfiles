#!/usr/bin/python3
"""input plaintext and shift"""
plainText = input("Insert your ciphertext: ")
shift = int(input("Enter your shift: "))
"""decrypt function"""


def decrypt(plainText, shift):
    cipherText = ""
    for ch in range(0, len(plainText)):
        if (ch + shift) < len(plainText):
            cipherText += plainText[ch]
            while ch < (len(plainText) - shift):
                ch += shift
                cipherText += plainText[ch]
    print ("Your ciphertext is: ", cipherText)
    return cipherText


decrypt(plainText, shift)
