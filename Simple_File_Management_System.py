from pathlib import Path

def run():
    """Main Program where the input from the user is asked and then broken into following commands"""
    while True:
        user_input = input().strip().split(maxsplit=1)
        command = user_input[0].upper()

        if command == 'Q':
            break

        try:
            if command == 'L':
                if '-' not in user_input[1]:
                    pathname = Path(user_input[1])
                    list_contents(pathname)
                elif '-' in user_input[1]:
                    if user_input[1][-2:] == '-r':
                        pathname = Path(user_input[1][:-3])
                        recurse(pathname)

                    elif '-f' in user_input[1]:
                        if '-r' not in user_input[1]:
                            pathname = Path(user_input[1][:-3])
                            only_files(pathname)
                        elif '-r' in user_input[1]:
                            indexr = user_input[1].index('-r')
                            pathname = Path(user_input[1][:indexr-1])
                            only_files(pathname, True)

                    elif '-s' in user_input[1]:
                        if '-r' not in user_input[1]:
                            index = user_input[1].index('-s')
                            filename = user_input[1][index + 3:]
                            pathname = Path(user_input[1][:index - 1])
                            specific(pathname, filename)
                        elif '-r' in user_input[1]:
                            indexr = user_input[1].index('-r')
                            indexs = user_input[1].index('-s')
                            pathname = Path(user_input[1][:indexr - 1])
                            filename = user_input[1][indexs + 3:]
                            specific(pathname, filename, True)
                    elif '-e' in user_input[1]:
                        if '-r' not in user_input[1]:
                            index = user_input[1].index('-e')
                            filex = user_input[1][index + 2:]
                            pathname = Path(user_input[1][:index - 1])
                        elif '-r' in user_input[1]:
                            indexr = user_input[1].index('-r')
                            indexe = user_input[1].index('-e')
                            pathname = Path(user_input[1][:indexr-1])
                            filex = user_input[1][indexe + 3:]
                            extension(pathname, filex, True)
                    else:
                        pathname = Path(user_input[1])
                        list_contents(pathname)
                    
            elif command == 'C':
                try:
                    if '-n' in user_input[1]:
                        index = user_input[1].index('-n')
                        filename = user_input[1][index+3:]
                        pathname = Path(user_input[1][:index-1])
                        create_file(pathname, filename)
                    else:
                        print("ERROR")
                except Exception:
                    print("ERROR")
            elif command == 'D':
                try:
                    pathname = Path(user_input[1])
                    delete_file(pathname)
                except Exception as e:
                    print("ERROR")
                
            elif command == "R":
                try:
                    pathname = Path(user_input[1])
                    read_file(pathname)
                except Exception as e:
                    print("ERROR") 
            
            else:
                print("ERROR")

        except IndexError:
            print("ERROR")

def print_list(lst):
    for element in lst:
        print(element)

def list_contents(path):
    """The 'L' command takes place which prints out all files and directories within given directory"""

    if path.is_dir():
        for file in path.iterdir():
            if file.is_file():
                print(file)
        for file in path.iterdir():
            if file.is_dir():
                print(file)
    else:
        print("No such file exists")

def extension(folder, search, recursive = False):
    '''Filters out files based on the extension asked'''

    file_list = []
    if not recursive:
        for file in folder.iterdir():
            str_file = str(file)
            sep = str_file.split('.')
            if search in sep:
                file_list.append(file)
        
        if not file_list:
            print("No such file found!")
        else:
            print_list(file_list)
    
    elif recursive:
        rec_list = recurse(folder, [], True)
        if rec_list:
            for file in rec_list:
                str_file = str(file)
                sep = str_file.split('.')
                if search in sep:
                    file_list.append(file)
            print_list(file_list)
        else:
            exit()

def specific(folder, search, recursive = False):
    """Only adds files which have specified name"""

    file_list = []
    if not recursive:
        for file in folder.iterdir():
            str_file = str(file)
            sep = str_file.split('\\')
            if search in sep:
                file_list.append(file)
        
        if not file_list:
            print("No such file exists")
        else:
            print_list(file_list)

    else:
        rec_list = recurse(folder, [], True)

        if rec_list:
            for file in rec_list:
                str_file = str(file)
                sep = str_file.split('\\')
                if search in sep:
                    file_list.append(file)
            print_list(file_list)
        else:
            exit()

def recurse(folder, file_list = [], only_files = False):
    """The recursion takes place which prints subdirectories and it's files"""

    if not only_files and folder.is_dir():
        for file in folder.iterdir():
            if file.is_file():
                print(file)

        for file in folder.iterdir():
            if file.is_dir():
                print(file)
                recurse(file, [])

    elif only_files and folder.is_dir():
        for file in folder.iterdir():
            if file.is_file():
                file_list.append(file)
        for file in folder.iterdir():
            if file.is_dir():
                recurse(file, file_list, True)
        return file_list

def only_files(folder, recursive = False):
    """To print only the files in the directory"""
    if folder.is_dir():
        if not recursive:
            for file in folder.iterdir():
                if file.is_file():
                    print(file)
            
        elif recursive:
            files = recurse(folder, [], True)
            print_list(files)

def create_file(folder, name):
    """Creating a file with the given name in specified directory"""
    suffix = '.dsu'
    name += suffix
    path = folder / name
    try:
        path.touch()
        print(path)
    except Exception as e:
        print("ERROR")

def delete_file(folder):
    """Deleting a file specified by the user"""

    try:
        if folder.suffix == '.dsu':
            folder.unlink()
            print(f'{folder} DELETED')
        else:
            print("ERROR")

    except Exception:
        print("ERROR")

def read_file(folder):
    """Prints the contents of a file"""

    try:
        if folder.suffix == '.dsu':
            file_size = folder.stat().st_size
            if file_size == 0:
                print("EMPTY")
            else:
                text = folder.read_text()
                print(text.strip())
        else:
            print("ERROR")

    except Exception as e:
        print("ERROR")

if __name__ == "__main__":
    run()