'''
textfile.txt:

Hi! It's a textfile.txt
Purpose: test
Bye.

'''
f = open('textfile.txt', 'r') # opens the file "textfile.txt" in read mode
f = open('textfile.txt', 'w') # opens the file "textfile.txt" in write mode
f = open('textfile.txt', 'a') # opens the file "textfile.txt" in append mode
f = open('textfile.txt', 'x') # creates a new file called "textfile.txt" and opens it


f = open('textfile.txt', 'r')
print(f.read()) # reads the entire file and prints it to the console
f.close() # closes the file

with open("textfile.txt") as f:
  print(f.read()) # the 'with' statement automatically closes the file after the block of code is executed
  print(f.read(5)) # reads the first 5 characters of the file 
  print(f.readline()) # reads the first line of the file
  print(f.readlines()) # reads all the lines of the file and returns them as a list

with open("textfile.txt") as f:
  for i in f:
    print(i) # iterates through each line in the file and prints it to the console