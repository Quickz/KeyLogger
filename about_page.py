from tkinter import *


class AboutPage:

    isOpen = False

    @staticmethod
    def open():
        if AboutPage.isOpen is True:
            return

        about_window = Toplevel()
        about_window.title('About')
        about_window.geometry('430x250')

        # adding callback to about window closing
        about_window.protocol(
            'WM_DELETE_WINDOW',
            lambda: AboutPage.on_close(about_window)
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

        AboutPage.isOpen = True

    @staticmethod
    def on_close(about_window):
        AboutPage.isOpen = False
        about_window.destroy()
