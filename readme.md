# Automatic Deleter

This is simple application that takes care of the house keep work necessary.
Ever downloaded some file and forgot to delete it later ?
is screenshots folder full of past photos you forgot to delete ?
**Automatic deleter** is for you.

## How it Works

You can select the Folders in which you want auto deleter to work in. And set the duration('days') after which the files will be deleted.
Each time you boot up your OS script will check if there are files older than the set duration for that folder and delete them if they are too old

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Things you need to run the software

```
Python 3
```

### Setup

Follow These Instruction.

1. Find a location where you want have your core_file and log file
   - Core file is file that contains the list of folder u want to enable Auto-Delete
   - Log File is a file that keeps track what is deleted
   - eg: say `C:\Users\(user_name)\documents` convert it as `C:\\Users\\(user_name)\\documents` and put it in `location` variable in `Automatic Deleter.py` and `Deleter_Script.py`
2. Then press `win+R` type `shell:startup`
   ![Run Window image](images\run_window.png)
3. In the new opened folder paste the `Deleter_Script.py`

Thats it !!🎉🎉🎉

## ⚒ Built With

- [Python 3](https://www.python.org/) - The Programming Language used.
- [Tkinter](https://wiki.python.org/moin/TkInter) - Tkinter is Python's de-facto standard GUI (Graphical User Interface) package.

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

---

> Feel free to star ⭐ this repository if you like what you see 😉.
