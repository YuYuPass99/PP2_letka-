'''
textfile.txt:

Hi! It's a textfile.txt
Purpose: test
Bye.

'''

with open("textfile.txt", "a") as f:
  f.write("Adding more content.") # appends the string "Adding more content." to the end of the file

#open and read the file after the appending:
with open("textfile.txt") as f:
  print(f.read()) 
'''
Output:
Hi! It's a textfile.txt
Purpose: test
Bye.Adding more content.
'''

with open("textfile.txt", "w") as f:
  f.write("Overwriting the file.") # overwrites the entire file with the string "Overwriting the file."

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read()) # Output: Overwriting the file.

f = open("myfile.txt", "x") # creates a new file called "myfile.txt" and opens it.
