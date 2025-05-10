#Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follow
fh = open('file/mbox-short.txt')

for line in fh:
  line = line.rstrip()
