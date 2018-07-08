import keyboard
import json
from tkinter import *
from tkinter import filedialog

def on_release(event):
    # print(event.name)
    global total_key_count
    total_key_count += 1

    add_key_press(event.name)
    # print(pressed_key_counts)

    list_box.delete(0, END)
    for key in pressed_key_counts:
        key_data = key + ': ' + str(pressed_key_counts[key]) + '\n'
        list_box.insert(END, key_data)

    label_text.set('Keystrokes: ' + str(total_key_count))


def start_logging_keys():
    keyboard.on_release(on_release)


def add_key_press(key):
    global pressed_key_counts
    global logged_keys
    if key not in pressed_key_counts:
        pressed_key_counts[key] = 1
    else:
        pressed_key_counts[key] += 1
    logged_keys += key + ' '


# saves the pressed key counts data
# in a JSON file or some other format
def save_data():

    file = filedialog.asksaveasfile(
        mode='w',
        initialdir='/',
        title='Save',
        filetypes=(('JSON (*.json)', '*.txt'), ('All files', '*.*')),
        defaultextension='.json'
    )

    if file:
        data = json.dumps(pressed_key_counts, indent=4)
        file.write(data)
        file.close()


def open_license_page():
    global license_page_is_open
    if license_page_is_open is True:
        return

    license_window = Toplevel()
    license_window.title('License')
    license_window.geometry('630x400')

    # adding callback to license window closing
    license_window.protocol(
        'WM_DELETE_WINDOW',
        lambda: on_license_page_close(license_window)
    )

    frame = Frame(license_window)
    frame.pack()

    text = Text(frame, width=80, height=25)

    license_file = open('LICENSE', 'r')
    if license_file:
        text.insert(INSERT, license_file.read())
        license_file.close()
    else:
        text.insert(INSERT, 'Error in loading the license')

    text.config(state=DISABLED)
    text.pack()

    license_page_is_open = True


def on_license_page_close(license_window):
    global license_page_is_open
    license_page_is_open = False
    license_window.destroy()


def open_about_page():
    global about_page_is_open
    if about_page_is_open is True:
        return

    about_window = Toplevel()
    about_window.title('About')
    about_window.geometry('430x250')

    # adding callback to about window closing
    about_window.protocol(
        'WM_DELETE_WINDOW',
        lambda: on_about_page_close(about_window)
    )

    frame = Frame(about_window)
    frame.pack()

    text = Text(frame, width=55, height=17)
    text.insert(
        INSERT,
        'An application that logs the pressed keys and '
        'counts the number of times each of them have been used.\n'
        'Source code: https://github.com/Quickz/KeyLogger'
    )

    text.config(state=DISABLED)
    text.pack()

    about_page_is_open = True


def on_about_page_close(about_window):
    global about_page_is_open
    about_page_is_open = False
    about_window.destroy()


pressed_key_counts = {}
total_key_count = 0
logged_keys = ''

license_page_is_open = False
about_page_is_open = False

window = Tk()

window.title('KeyLogger')
window.geometry('300x200')

frame = Frame(window)
frame.pack()

label_text = StringVar()
label = Label(frame, textvariable=label_text)
label_text.set('Keystrokes: 0')
label.pack()

list_box = Listbox(frame, width=25, height=8, font=('Helvetica', 12))
list_box.pack(side='left', fill='y')

scrollbar = Scrollbar(frame, orient='vertical')
scrollbar.config(command=list_box.yview)
scrollbar.pack(side='right', fill='y')

list_box.config(yscrollcommand=scrollbar.set)


def donothing():
    pass


menubar = Menu(window)

# File
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Save...", command=save_data)
filemenu.add_command(label="Exit", command=window.quit)

# Help
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)

helpmenu.add_command(label="License...", command=open_license_page)
helpmenu.add_command(label="About...", command=open_about_page)

window.config(menu=menubar)


start_logging_keys()
window.mainloop()
