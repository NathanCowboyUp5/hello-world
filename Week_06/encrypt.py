"""
Project: encrypt.py
Author: Nathan Stroup

This project specializes in encrypting a user's provided message through a Caesar
cipher based on its provided content and distance variable.

Project steps:
1. The user inputs are:
    1. userProvidedMessage
    2. userMessageDistanceVariable
2. Key Variable:
    userPlainTextMessage = "" (This becomes a user's final encrypted message at the end of the program.)
3. Computations:
    1.Inside a FOR loop, the amount of characters (ch) in a user's message are encrypted through the Caesar cipher:
           1. The encryption order variable equals the ord(ch) item.
            2. The encryption cipher variable is equal to (The encryption order variable minus 32 plus the user's message
                distance value) plus thirty two. The ninety-five percent helps its final value remain in range of the
                ASCII's ninety-five computable items.
            3. The user's plaintext message adds to the encryption cipher variable's character value.
4. The output is the user's encrypted message, which is "userPlainTextMessage".
"""

#User input prompts for their message and distance variable.
userProvidedMessage = input("Please insert a message: ")
userMessageDistanceVariable = int(input("Please insert the provided message's distance variable: "))
userPlainTextMessage = ""

#Encryption process for the user's provided message.
for ch in userProvidedMessage:
    encryptionOrderVariable = ord(ch)
    encryptionCipherVariable = (encryptionOrderVariable - 32 + userMessageDistanceVariable) + 32 % 95  #95 is the amount of printable ASCII characters (32 to 126).
    userPlainTextMessage += chr(encryptionCipherVariable)
    
#Output encrypted message.
print("The encrypted message is:", userPlainTextMessage)
    
    
    
    



