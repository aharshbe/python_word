import wp_f

while (1):
    print("What would you like to do? ")
    print("Enter: ")
    print("c:\t create a file")
    print("r:\t read a file")
    print("l:\t to list files")
    print("d:\t delete a file")
    print("\n")

    #get input and asses it
    i = input()
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
        print("either type 'exit' to exit or c or d")
        continue
