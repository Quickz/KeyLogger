import keyboard
from tkinter import *


def on_release(event):
    # print(event.name)
    global keystroke_count
    keystroke_count += 1

    add_key_press(event.name)
    # print(keys_pressed)

    list_box.delete(0, END)
    for key in keys_pressed:
        key_data = key + ': ' + str(keys_pressed[key]) + '\n'
        list_box.insert(END, key_data)

    label_text.set('Keystrokes: ' + str(keystroke_count))


def start_logging_keys():
    keyboard.on_release(on_release)


def add_key_press(key):
    global keys_pressed
    if key not in keys_pressed:
        keys_pressed[key] = 1
    else:
        keys_pressed[key] += 1


keys_pressed = {}
keystroke_count = 0


# start_logging_keys()
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

start_logging_keys()
window.mainloop()
