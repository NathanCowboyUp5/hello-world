"""
Project: decrypt.py
Author: Nathan Stroup

This project focuses on unlocking a user's encrypted message through the Caesar
Cipher derived from their provided plaintext and its distance variable.

Program Steps:
1. The user inputs are:
    1. userEncryptedMessage
    2. encryptedMessageDistanceVariable
2. Crucial Variable:
    userPlainTextMessage = "" (This becomes an individual's decrypted announcement after this program ends).
3. Computations:
    1. Inside a FOR loop, the number of characters (ch) inside a user's locked message are opened through a Caesar cipher:
            1. The decryption order variable equals the ord(ch) item.
            2. The decryption cipher variable is equal to (The decryption order variable minus 32 minus the user's encrypted message
                distance variable) plus thirty two. The ninety-five percent helps it completed value remain in range of the
                ASCII's ninety-five computable values.
            3. The user's plaintext announcment adds to the decryption cipher variable's character value.
4. The output is the user's decrypted message, which is "userPlainTextMessage".
"""
#User input prompts for their encrypted message and its distance variable.
userEncryptedMessage = input("Please insert your encrypted message: ")
encryptedMessageDistanceVariable = int(input("Please insert your message's distance variable: "))
userPlainTextMessage = ""

#Decryption process of user's message.
for ch in userEncryptedMessage:
    decryptedOrderVariable = ord(ch)
    decryptionCipherVariable = (decryptedOrderVariable - 32 - encryptedMessageDistanceVariable) + 32 % 95   #95 = the amount of printable ASCII characters (32 to 126).
    userPlainTextMessage += chr(decryptionCipherVariable)

#Output the decrypted message.
print("The decrypted message is:", userPlainTextMessage)
