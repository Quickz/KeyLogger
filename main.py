import keyboard
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
        file.write(str(pressed_key_counts))
        file.close()


pressed_key_counts = {}
total_key_count = 0
logged_keys = ''

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

helpmenu.add_command(label="License...", command=donothing)
helpmenu.add_command(label="About...", command=donothing)

window.config(menu=menubar)

start_logging_keys()
window.mainloop()
