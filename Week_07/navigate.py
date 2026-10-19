"""
Project: navigate.py
Author: Nathan Stroup

This program focuses on helping a user view specific lines within their provided text document
through its assigned digits, which are placed inside a list. Additionally, it runs inside a WHILE loop, where
an inserted value's data is outputted and requests someone to provide another. These items stretch from one to
the document's maximum amount of code. However, if a user enters zero, the project concludes. Overall, this tool
prints a digit's targeted content.

Program Steps:
1. User inputs are:
    1. userFileName
        1. Note: The user's provided text document is opened inside its read mode ("r"),
            which is labeled as "files".
        2. The user file's lines, "files", are organized into the "list()" command.
        3. The user's complete file lines are equal to its offered lines
            inside the "(len)" tool, which identifies their amount of elements.
2. A Crucial Variable is:
    1. beginningProvidedFileValue = 1
3. Computations (Inside a WHILE loop and if-else statement):
    1. while True:
        1. The user is asked to insert a line number from their inserted document that run from one
            to its maximum digit. They may also enter zero ("0") to end the project.
        2. If the user's beginning file value (1) is less than or equal to their provided line digit,
            while it is less than or equal to the document's complete amount of lines, their inserted
            digit is subtracted by one to accurately output its content.
        3. If a person's offered value is equal to zero ("0"), the program ends.
        4. If a user's provided line number is not located in their file, they are ordered to
            insert another one that is.
4. The outputs are either:
    1. A notification statement that informs a user their program's targeted line has been located.
    2. A message that says the project has concluded, which is due to the user entering the line number zero.
    3. An alert that instructs a user to insert a different line value if their previous
        one is not present inside a specfic document.
"""

#User input prompts for a filename, as its content is formatted inside a list.
userFileName = input("Please insert the name of your file (Example: 'myfile.txt'): ")
files = open(userFileName, "r")
providedFileLines = list(files)
providedFileTotalLines = len(providedFileLines)

#Crucial Variable
beginningProvidedFileValue = 1

#Process of outputting a text file's line through a WHILE loop and if-else statement.
while True:
    print("The", userFileName, "features", providedFileTotalLines, "lines.")
    userProvidedLineNumber = int(input("Please insert a line number from your file (or '0' to end): "))
    if beginningProvidedFileValue <= userProvidedLineNumber <= providedFileTotalLines: 
        print(providedFileLines[userProvidedLineNumber - 1])
    elif userProvidedLineNumber == 0:
        print("You have closed the file. The program has concluded.")
        break
    else:
        print("This line number is not present. Please enter a value within range of 1 and", providedFileTotalLines)
    
    
    

