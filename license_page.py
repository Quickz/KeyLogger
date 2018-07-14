from tkinter import *


class LicensePage:

    isOpen = False

    @staticmethod
    def open():
        if LicensePage.isOpen is True:
            return

        license_window = Toplevel()
        license_window.title('License')
        license_window.iconbitmap(r'icon.ico')
        license_window.geometry('630x400')

        # adding callback to license window closing
        license_window.protocol(
            'WM_DELETE_WINDOW',
            lambda: LicensePage.on_close(license_window)
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

        LicensePage.isOpen = True

    @staticmethod
    def on_close(license_window):
        LicensePage.isOpen = False
        license_window.destroy()
