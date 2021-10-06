import csv
import os
from tkinter import Tk, filedialog
from tkinter import NO, CENTER, W, RIGHT, Y, N
from tkinter.ttk import Button, Entry, Frame, Label, LabelFrame, Labelframe, Scrollbar, Style, Treeview


CORE_FILE_PATH = "C:\\Users\\saif1\\OneDrive\\Documents\\delete_folders_list.csv"
LOGS_FILE_PATH = "C:\\Users\\saif1\\OneDrive\\Documents\\delete_log.txt"


def check_core_file_exists(): return os.path.isfile(CORE_FILE_PATH)


def create_core_file():
    with open(CORE_FILE_PATH, mode='w', newline='') as csv_file:
        fieldnames = ['folder_path', 'duration']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
    remove_all_data_from_tree()


def read_core_file():
    if(not check_core_file_exists()):
        print("File Does Not exist! Creating new File")
        create_core_file()
    else:
        isFileValid = True
        with open(CORE_FILE_PATH) as core_file:
            core_reader = csv.DictReader(
                core_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            count = 0
            for row in core_reader:
                print(row)
                if list(row.keys()) != ['folder_path', 'duration']:
                    isFileValid = False
                    break
                addToTree(index=count, values=(
                    [count]+list(row.values())), iid=count, text='')
                count += 1
        if not isFileValid:
            print("Invalid File Provided. Re-Creating the File")
            create_core_file()


def add_data_to_file(folder_path, duration):
    with open(CORE_FILE_PATH, mode='a', newline='') as csv_file:
        fieldnames = ['folder_path', 'duration']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writerow({
            'folder_path': folder_path,
            'duration': str(duration)
        })
        print("Folder Added")


# Tree operations
def remove_all_data_from_tree():
    for record in treeview.get_children():
        treeview.delete(record)


def setUpTreeColumn():
    treeview['columns'] = ('Id', 'File Dir', 'Duration')
    treeview.column('#0', width=0, stretch=NO)
    treeview.column('Id', anchor=W, minwidth=30, width=30, stretch=NO)
    treeview.column('File Dir', anchor=CENTER, width=80)
    treeview.column('Duration', anchor=CENTER,
                    width=80, minwidth=80, stretch=NO)


def setUpTreeHeading():
    treeview.heading('#0', text='', anchor=CENTER)
    treeview.heading('Id', text='Id', anchor=W)
    treeview.heading('File Dir', text='File Dir', anchor=CENTER)
    treeview.heading('Duration', text='Duration', anchor=CENTER)


def addToTree(index, values, iid, text):
    treeview.insert(parent='', index=index, iid=iid, text=text, values=values)


def minify(p, val):
    if len(p) <= val:
        return p
    val -= 3
    sv = val//2
    return p[0:sv] + "..."+p[-sv:]

# UI Operations


def add_data():
    folder_path = selected_label.cget('text')
    duration = dur_entry.get()
    print(folder_path, duration)
    add_data_to_file(folder_path=folder_path, duration=duration)
    remove_all_data_from_tree()
    read_core_file()


def remove_data():
    if treeview.selection() == () or treeview.selection() == None or len(treeview.selection()) == 0:
        return
    iid = treeview.selection()[0]
    if iid == None or iid == "":
        return
    treeview.delete(iid)
    records = []
    for child in treeview.get_children():
        records += [treeview.item(child)["values"]]
    print(records)
    create_core_file()
    for record in records:
        add_data_to_file(folder_path=record[1], duration=record[2])
    read_core_file()


def pick_folder():
    location = filedialog.askdirectory()
    if location == None or location.strip() == "":
        selected_label.config(text="(None Selected)")
    else:
        selected_label.config(text=minify(location, 60))


root = Tk()

# # configure the root window
root.title('Theme Demo')
root.geometry('400x400')
style = Style(root)
style.theme_use("xpnative")

# Creating Tree Frame
tree_frame = Frame(root)
tree_frame.pack(padx=10, pady=(10, 0), fill="x", expand="yes")

# Scroll Bar for tree frame
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
treeview = Treeview(tree_frame, yscrollcommand=tree_scroll.set,
                    selectmode="extended")

treeview.pack(fill="x", expand="yes")
tree_scroll.config(command=treeview.yview)

# Column
setUpTreeColumn()

# Heading

setUpTreeHeading()

# Adding Data

# addToTree(index=0, iid=0, text='', values=('1', 'Vineet', 'Alpha'))
# addToTree(index=1, iid=1, text='', values=('2', 'Anil', 'Bravo'))
# addToTree(index=2, iid=2, text='', values=('3', 'Vinod', 'Charlie'))


# UI Creation and placement
file_frame = Labelframe(root, text="Selection")
file_frame.pack(padx=10, pady=(5, 0), ipady=5,
                ipadx=10, fill="x", expand="yes")

select_label = Label(file_frame, text="Pick Your Folder")
select_label.grid(row=0, column=0, padx=(10, 0))

select_button = Button(file_frame, text="Select", command=pick_folder)
select_button.grid(row=0, column=1, sticky=W, padx=(0, 10))

selected_label = Label(file_frame, text="(None Selected)")
selected_label.grid(row=1, column=0, columnspan=4, pady=(5, 0))

dur_label = Label(file_frame, text='Duration')
dur_label.grid(row=0, column=2, padx=(0, 5))

dur_entry = Entry(file_frame)
dur_entry.grid(row=0, column=3, sticky=W)


command_frame = LabelFrame(root, text="Comamnd")
command_frame.pack(padx=10, pady=(5, 10), ipady=5, fill="x", expand=True)
add_button = Button(command_frame, text="Add", command=add_data)
remove_button = Button(command_frame, text="Remove", command=remove_data)
add_button.pack(side='left', fill="x", expand=True)
remove_button.pack(side='right', fill="x", expand=True)


# INIT OPERATION
read_core_file()

root.mainloop()
