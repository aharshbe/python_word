#this function writes a file from scratch

#import date and time
import datetime
#import os to remove file
import os

def get_multiline_input():
    lines = []
    while (1):
        line = input()
        if line:
            lines.append(line)
        else:
            break
    input_val = '\n'.join(lines)
    return input_val

#create a file
def create_file():
    now = datetime.datetime.now()
    name_of_file = input("New file name: ")
    target = open(name_of_file, 'w')
    new_line = "\n"
    print(new_line + name_of_file + " " + str(now))
    print("Insert mode..." + new_line)
    top_of_file = "File " + name_of_file + ": " + str(now) + new_line
    contents = get_multiline_input()
    #write contents to file
    target.write(top_of_file)
    target.write(new_line)
    target.write(contents)
    target.write(new_line * 2)
    #save contents of the file
    target.close()

#delete a file
def delete_file():
    name_of_file = input("Name of file: ")
    os.remove(name_of_file)
    print("File removed.")
    print("\n")

#list files
def list_files():
    files = os.listdir(".")
    i = 0
    while (i < len(files)):
        print("file " + str(i) + " " + files[i])
        i += 1

#read a file
def read_file():
    name_of_file = input("File to read: ")
    target = open(name_of_file)
    print(target.read())
    target.close()