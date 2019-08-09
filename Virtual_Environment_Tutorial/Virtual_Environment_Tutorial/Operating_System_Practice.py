import os

os.chdir(r'C:\Users\Phyli\OneDrive\Documents\Hamilton Stuff\Coding Projects')
print(os.getcwd)

file_location = r'C:\Users\Phyli\OneDrive\Documents\test.txt'
document = open(file_location)
contents = document.read()
print(contents)
