"""This module contains main function."""
# a2.py

# Replace the following placeholders with your information.

# AANYA AGRAWAL
# AANYAA2@UCI.EDU
# 50709128

from Profile import Profile, Post
from ui import *


def main():
    """Main function to run user command."""
    print("enter admin or user mode: ", end="")
    mode = input()

    while True:
        if mode.lower() not in ["user", "admin"]:
            print("Invalid mode.")
            break

        choice = get_data(mode)
        if choice.lower() == "q":
            break

        command = choice.split(" ", 1)[0]
        if len(choice.split(" ", 1)) > 1:
            arguments = choice.split(" ", 1)[1].split(" ")
        else:
            arguments = []

        if command == "L":
            list_files_and_directories(arguments[0])

        elif command == "C":
            create_new_file(arguments[0], arguments[1], arguments[2], arguments[3], arguments[4])

        elif command == "D":
            delete_file(arguments[0])

        elif command == "R":
            read_file_content(arguments[0])

        elif command == "O":
            open_a_dsu_file(arguments[0])

        elif command == "E":
            data = {}
            for arg in arguments:
                key, value = arg.split(":")
                data[key] = value
            edit_profile(data, e_path)

        elif command == "P":
            profile = Profile()
            profile.load_profile(e_path)
            if arguments[0] == "-all":
                print(profile)
            elif arguments[0] == "-post":
                print(profile.get_post(int(arguments[1])))

        else:
            print("Invalid command.")


if __name__ == '__main__':
    main()
