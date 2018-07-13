import keyboard
import json
from tkinter import *
from tkinter import filedialog
from about_page import AboutPage
from license_page import LicensePage


def on_release(event):

    global file_dialog_is_open
    global app_paused
    if file_dialog_is_open or app_paused:
        return

    add_key_press(event.name)
    update_key_list()
    label_text.set('Keystrokes: ' + str(total_key_count))


# updates the list box that
# contains the key counts
def update_key_list():
    # clearing the list
    list_box.delete(0, END)

    # filling it up with new data
    for key in pressed_key_counts:

        key_percentage = get_key_percentages(key)

        if key_percentage <= 0.01:
            key_percentage = 'less than 0.01'
        else:
            key_percentage = round(key_percentage, 2)

        key_data = key + ': ' +\
            str(pressed_key_counts[key]) + ', ' +\
            str(key_percentage) + '%\n'

        list_box.insert(END, key_data)


# tells what percentage
# does the selected key take
# in the key list
def get_key_percentages(key):
    return pressed_key_counts[key] / total_key_count * 100


def start_logging_keys():
    keyboard.on_release(on_release)


def add_key_press(key):

    global pressed_key_counts
    global logged_keys
    global total_key_count

    total_key_count += 1

    # counting how many times
    # each key has been pressed
    if key not in pressed_key_counts:
        pressed_key_counts[key] = 1
    else:
        pressed_key_counts[key] += 1

    # saving the actual key that was pressed
    logged_keys.append(key)


# opens a save dialog window and
# saves the pressed key counts data
# in a JSON file or some other format
def save_data():

    global file_dialog_is_open
    file_dialog_is_open = True

    file = filedialog.asksaveasfile(
        mode='w',
        initialdir='/',
        title='Save',
        filetypes=(('JSON (*.json)', '*.txt'), ('All files', '*.*')),
        defaultextension='.json'
    )

    if file:
        data = {
            'key counts': pressed_key_counts,
            'logged keys': logged_keys
        }
        data = json.dumps(data, indent=4)

        file.write(data)
        file.close()

    file_dialog_is_open = False


# temporarily stops the app
# from logging the keyboard input
# or resumes it if called again
def on_pause_button_click():
    global app_paused
    app_paused = not app_paused
    if app_paused:
        pause_button.configure(text='Resume')
    else:
        pause_button.configure(text='Pause')


pressed_key_counts = {}
total_key_count = 0
logged_keys = []

file_dialog_is_open = False
app_paused = False

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

helpmenu.add_command(label="License...", command=LicensePage.open)
helpmenu.add_command(label="About...", command=AboutPage.open)

window.config(menu=menubar)


# Bottom
bottom_frame = Frame(window)
bottom_frame.pack()

pause_button = Button(
    bottom_frame,
    text='Pause',
    width=7,
    command=on_pause_button_click)
pause_button.pack()


start_logging_keys()
window.mainloop()
