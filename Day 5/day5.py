""" Python program that reads a tet file and counts the number of lines in it."""

'''I have used exception handling to handle the file not found error. If the file is not found, the except block will be executed and the error message will be printed.'''
try:
    with open("data.txt", "r") as test_file:
        for count, line in enumerate(test_file):
            pass
    print("Total number of files: ", count + 1)
except FileNotFoundError:
    print("File not found")
