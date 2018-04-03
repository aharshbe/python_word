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
            s = input("Save file? (y/n)")
            if (s == 'y'):
                break
            else:
                lines.append(line)
    input_val = '\n'.join(lines)
    return input_val

#create a file
def create_file():
    os.system('clear')
    now = datetime.datetime.now()
    name_of_file = input("New file name: ")
    target = open(name_of_file, 'w')
    new_line = "\n"
    print(new_line + name_of_file + " " + str(now))
    if (name_of_file.endswith(".c") == True):
        print("Create C file.." + new_line)
    else:
        print("Insert mode..." + new_line)
    top_of_file = "File " + name_of_file + ": " + str(now) + new_line
    contents = get_multiline_input()
    #write contents to file
    if (name_of_file.endswith(".c")  == False):
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
    print("\n")
#read a file
def read_file():
    name_of_file = input("File to read: ")
    target = open(name_of_file)
    print(target.read())
    target.close()
