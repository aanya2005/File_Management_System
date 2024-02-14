"""This file handles all the functions."""
# ui.py

# Replace the following placeholders with your information.

# AANYA AGRAWAL
# AANYAA2@UCI.EDU
# 50709128

from Profile import *
from pathlib import Path


def edit_profile(data, e_path):
    """ Allow user to edit function."""
    if not Path(e_path).exists():
        print("Profile not found.")
        return

    profile = Profile()
    profile.load_profile(e_path)

    for key, value in data.items():
        if value:
            if key == "-usr":
                profile.username = value
            elif key == "-pwd":
                profile.password = value
            elif key == "-bio":
                profile.bio = value
            elif key == "-addpost":
                post = Post(value)
                profile.add_post(post)
            elif key == "-delpost":
                profile.del_post(int(value))

    profile.save_profile(e_path)


def list_files_and_directories(directory):
    """User can list files and directories."""
    p = Path(directory)
    files, directories = [], []

    for obj in p.iterdir():
        if obj.is_file():
            files.append(obj)
        else:
            directories.append(obj)

    files.sort()
    directories.sort()

    for f in files:
        print(f)

    for d in directories:
        print(d)


def create_new_file(directory, filename, username, password, bio):
    """To create new file."""
    global e_path

    if not Path(directory).exists():
        print("Directory does not exist.")
        return

    file_path = Path(directory) / (filename + ".dsu")
    if file_path.exists():
        open_a_dsu_file(file_path)
    else:
        file_path.touch()
        print(file_path)
        e_path = file_path
        profile = Profile(username=username, password=password)
        profile.save_profile(file_path)


def open_a_dsu_file(path):
    """To open a dsu file."""
    global e_path
    e_path = path

    print("File loaded successfully")
    profile = Profile()
    profile.load_profile(e_path)
    print(f"Username: {profile.username}")
    print(f"Password: {profile.password}")
    print(f"Bio: {profile.bio}")


def delete_file(path):
    """To delete a file."""
    if not Path(path).exists():
        print("File not found.")
        return

    Path(path).unlink()
    print(f"{path} DELETED")


def read_file_content(file_path):
    """To read a file."""
    if not Path(file_path).exists():
        print("File not found.")
        return

    with open(file_path, "r") as f:
        content = f.read()
        if content:
            print(content.strip())
        else:
            print("EMPTY")


def get_data(mode):
    """User vs Admin mode."""
    if mode == "admin":
        choice = input()
        return choice
    elif mode == "user":
        choice = ""
        option = user_mode()
        if option == "L":
            p = get_path()
            rc = input("R for recursive, N for non-recursive : ")
            if rc == "R":
                rc = "-r"
                p = p + " " + rc
            choice = option+" "+p
            print("Options of the 'L' command")
            print("After the path you can enter like the following : ")
            print("-r : Output directory content recursively.")
            print("-f : Output only files, excluding directories.")
            print("-s : Output only files that match a given file name.")
            print("-e : Output only files that match a given file extension.")
            print("-n : No option selected")
            print("Dont forget to enter - symbol before the option")
            ch = input("Enter your choice: [-f/-s/-e/-n] : ")
            if ch == "-e":
                extention = input("Enter file extension(eg: jpg, png, txt): ")
                choice = option+" " + p + " " + ch + " " + extention
                return choice
            elif ch == "-s":
                file_name = input("Enter file name,<filename.extension>: ")
                choice = option + " " + p + " " + ch + " " + file_name
                return choice
            elif ch == "-f":
                choice = option + " " + p + " " + ch
                return choice
            return choice
        elif option == "D" or option == "R":
            p = get_path()
            f = get_file()
            choice = option+" "+p+"/"+f
            return choice
        elif option == "C":
            p = get_path()
            f = get_file()
            choice = option+" "+p+" "+"-n"+" "+f
        elif option == "E":
            choice = edit_menu_c()
            return choice
        elif option == "P":
            choice = print_menu_p()
            return choice
        elif option == "O":
            p = get_path()
            f = get_file()
            choice = option+" "+p+"/"+f
            return choice
        elif option == "Q":
            choice = option.lower()
            return choice
        return choice


def user_mode():
    """User mode options."""
    print("L - command to load the file.")
    print("D - Delete the file.")
    print("R - Read the contents of a file.")
    print("C - Create a new file in the specified directory.")
    print("O - Open an existing file of the type dsu")
    print("Q - to exit the program")
    print("E - Edit an existing file in the specified directory")
    print("P - Print data stored in the DSU file loaded by C or O commands")
    print("NOTE : E and P will only work with C or O commands")
    option = input("Enter the mode [L,D,R,C,O,Q,E,P] : ").upper()
    return option


def get_path():
    """Getting path from user."""
    p = input("Enter the path : ")
    return p


def get_file():
    """Getting file from user."""
    f = input("Enter the file name along with extension : ")
    return f


def edit_menu_c():
    """User mode editting menu."""
    choice = "E "
    while True:
        print("To edit the file please use the following menu options : ")
        print("U: to edit the username of the file")
        print("P : to edit the password of the file")
        print("B : to edit the bio of the file")
        print("A : to add the post to the file")
        print("D : to delete the post using the post id of the file")
        print("N : For no more updates")
        option = input("Enter your option (U/P/B/A/D/N) : ").upper()
        if option == "U":
            new_user = input("Enter the new username: ").replace(" ", "")
            choice += "-usr "+new_user
        elif option == "P":
            new_pass = input("Enter the new password : ").replace(" ", "")
            choice += "-pwd "+new_pass
        elif option == "B":
            new_bio = input("Enter the bio : ")
            choice += "-bio " + new_bio
        elif option == "A":
            new_post = input("Enter the post : ")
            choice += "-addpost "+new_post
        elif option == "D":
            delete_post = input("Enter the post ID you want to delete : ")
            choice += "-deletepost "+delete_post
        elif option == "N":
            break
        else:
            print("Invalid Input")
    return choice


def print_menu_p():
    """Printing in user mode."""
    choice = "P "
    while True:
        print("To print the file choose from the following option : ")
        print("U:  Prints the username stored in the profile object")
        print("P : Prints the password stored in the profile object")
        print("B : Prints the bio stored in the profile object")
        print("PO : Prints all posts stored in profile object with their ID")
        print("PID : Prints post identified by ID")
        print("A : Prints all content stored in the profile objects")
        print("N : No more printing")
        option = input("Enter your option (U/P/B/PO/PIB/A/N) : ").upper()
        if option == "U":
            choice += "-usr "
        elif option == "P":
            choice += "-pwd "
        elif option == "B":
            choice += "-bio "
        elif option == "PO":
            choice += "-posts "
        elif option == "PID":
            pid = int(input("Enter the post ID you want to print : "))
            choice += "-post "+str(pid)+" "
        elif option == "A":
            choice += "-all "
            break
        elif option == "N":
            break
        else:
            print("Invalid Input")
    return choice
