"""
Project: copyfile.py
Author: Nathan Stroup

This program focuses on asking an individual for two text documents.
Following this, their first document's data is copied to the second item.

Project Steps:
1. The inputs are:
    1. firstTextFile
    2. secondTextFile
2. Computations:
    1. The first text file is identified as "originalTextFile", and it is viewed in its read mode ("r").
    2. The second text file is labeled as "f", which is opened in the write mode ("w").
    3. Inside a FOR loop, the second text document receives the first one's items through the
        "f.write(content)" command.
    4. The "f.close()" statement closes both files.
3. The outputs are:
    1. The original text file's details being added to the second one.
    2. A message confirming the first text file's content was transferred to the second one.
"""

#User inputs for two text documents.
firstTextFile = str(input("Please insert the name of your first text file (Example: 'myfile.txt'): "))
secondTextFile = str(input("Please insert the name of your text file receiving data (Example: 'myfile.txt'): "))

#The user's provided text files being edited.
originalFile = open(firstTextFile, "r")
f = open(secondTextFile, "w")
for line in originalFile:
    f.write(line)
f.close()

#Output results.
print("The", firstTextFile, "file's content has been duplicated to", secondTextFile, "!")
    
