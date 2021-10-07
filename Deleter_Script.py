import datetime
from os import name
import os.path
from pathlib import Path
import csv
CORE_FILE_PATH = "C:\\Users\\saif1\\OneDrive\\Documents\\delete_folders_list.csv"
LOGS_FILE_PATH = "C:\\Users\\saif1\\OneDrive\\Documents\\delete_log.txt"


def check_core_file_exists(): return os.path.isfile(CORE_FILE_PATH)


def printl(str):
    print(str)
    with open(LOGS_FILE_PATH, 'a+') as f:
        f.write(str+'\n')
        pass


def check_file_validity():
    isFileValid = True
    with open(CORE_FILE_PATH) as core_file:
        core_reader = csv.DictReader(
            core_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in core_reader:
            if list(row.keys()) != ['folder_path', 'duration']:
                isFileValid = False
                break
    return isFileValid


def delete_operation(folder_path, duration):
    printl(f"Folder Path : {folder_path}")
    dir = Path(folder_path)
    for file in dir.iterdir():
        if Path(file).is_file():
            file = Path(file)
            mod_date = datetime.datetime.fromtimestamp(file.stat().st_mtime)
            cur_date = datetime.datetime.today()
            if (cur_date - mod_date).days > duration:
                delete_file(file, (cur_date - mod_date).days)


def delete_file(file, d):
    printl(f"Deleting File {file.name}.")
    Path.unlink(file)


# Main Script
def start_script():
    if check_core_file_exists() and check_file_validity():
        with open(CORE_FILE_PATH) as core_file:
            core_reader = csv.DictReader(
                core_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            for row in core_reader:
                if os.path.isdir(row['folder_path']) and int(row['duration']) >= 0:
                    delete_operation(row['folder_path'], int(row['duration']))
                else:
                    printl(f"{row['folder_path']} Folder Not Found")
    else:
        printl("Core File Not Found | Core File Invalid!")


start_script()
