import wp_f
import os

while (1):
    print("What would you like to do? ")
    print("c:\t create a file")
    print("r:\t read a file")
    print("l:\t to list files")
    print("d:\t delete a file")
    print("exit:\t to exit")
    print("\n")

    #get input and asses it
    i = input()
    if (i != 'd' and i[0] != 'r'):
        os.system("clear")
    if (i == 'c'):
        wp_f.create_file()
    elif (i == 'd'):
        wp_f.delete_file()
    elif (i == 'r'):
        wp_f.read_file()
    elif (i == "exit"):
        break
    elif (i == 'l'):
        wp_f.list_files()
    else:
        print("Enter an option, e.g., 'c', 'r', 'l', 'd', or type 'exit' to exit")
        print("\n")
        continue
