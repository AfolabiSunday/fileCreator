def filecreator():
    yes = set(['yes', 'y', 'ye', ''])
    no = set(['no', 'n'])
    prompt ='>>>>>>>   '
    print("Hi, welcome to text file creator 2019 ")
    print("To get started, give a name to your file (without extension)")
    filename = input(prompt)
    print("awesome, please provide the content of the file")
    content = input(prompt)

    confirm = input("> do you want ot continue with the creation of file " + filename + ".txt? (yes/No) ").lower()
    if confirm in yes:
        textfile = open(filename + ".txt", "w")
        textfile.write(content)
        textfile.close()
        print("File successfully Created. ")
    elif confirm in no:
        print("ok, nothing will happen")
    new_file =input(prompt+"Will you like to create a new file? ")
    if new_file in yes:
            return filecreator()
    elif new_file in no:
            print("thanks for using this edition of file creator")
                        
    else:
        print("you have enter an invalid entry, please run the program again")
        



filecreator()
