
from pathlib import Path
import sys
from colorama import Fore, Style


def look_in_directory(directory, tabulation=0):
        for path in directory.iterdir():
            if path.is_dir():

                print (f"{" " * tabulation}{Fore.GREEN}{path.name}/ {Style.RESET_ALL}")
                look_in_directory(path, tabulation + 4)
               
            elif path.is_file():
                print (f"{" " * tabulation}{Fore.RED}{path.name} {Style.RESET_ALL}")

def main():

    directory = Path(sys.argv[1])

    if not directory.exists():
        print("Directory does not exist")
        sys.exit(1)

    look_in_directory(directory)

if __name__ == "__main__":
    main()


