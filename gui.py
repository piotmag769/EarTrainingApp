import tkinter as tk
from tkinter import *
from tkinter.ttk import *


initial = tk.Tk()
initial.geometry("700x500")
initial.wm_resizable(False, False)

# we can split different windows into different clasees + modules or sth
class App:
    def __init__(self, root):
        self.root = root

        self.current_mode = tk.IntVar()
        self.current_instrumnet = tk.IntVar()
        self.current_ex_type = tk.IntVar()

        self.mode_label = tk.Label(
            text="Current mode: EASY",
            font=('Comic Sans MS', 12, 'bold italic'),
        )

        self.instrument_label = tk.Label(
            text="Instrument picked: PIANO",
            font=('Comic Sans MS', 12, 'bold italic'),
        )

        self.ex_type_label = tk.Label(
            text = "Exercise picked: INTERVALS",
            font=('Comic Sans MS', 12, 'bold italic'),
        )

        self.easy_button = tk.Button(
            root,
            bg="green",
            fg="white",
            width=15,
            text="EASY",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_mode(0)
        )

        self.medium_button = tk.Button(
            root,
            bg="green",
            fg="white",
            width=15,
            text="MEDIUM",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_mode(1)
        )

        self.hard_button = tk.Button(
            root,
            bg="green",
            fg="white",
            width=15,
            text="HARD",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_mode(2)
        )

        self.piano_button = tk.Button(
            root,
            bg="purple",
            fg="white",
            width=15,
            text="Piano",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_instrument(0)
        )

        self.guitar_button = tk.Button(
            root,
            bg="purple",
            fg="white",
            width=15,
            text="Guitar",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_instrument(1)
        )

        self.trumpet_button = tk.Button(
            root,
            bg="purple",
            fg="white",
            width=15,
            text="Trumpet",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_instrument(2)
        )

        self.intervals_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Intervals",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_ex_type(0)
        )

        self.triads_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Triads",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_ex_type(2)
        )

        self.dom_seventh_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Dominant 7th",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_ex_type(1)
        )

        self.start_button = tk.Button(
            root,
            bg="red",
            fg="white",
            width=15,
            text="START!",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.openNewWindow()

        )

        self.mode_label.grid(row=0, column=3)
        self.mode_label.grid(row=1, column=3)

        self.mode_label.place(x=375, y=25, anchor="center")
        self.instrument_label.place(x = 375, y=50, anchor="center")
        self.ex_type_label.place(x = 375, y = 75, anchor="center")
        self.easy_button.place(x=100, y=100)
        self.medium_button.place(x=300, y=100)
        self.hard_button.place(x=500, y=100)
        self.piano_button.place(x=100, y=200)
        self.guitar_button.place(x=300, y=200)
        self.trumpet_button.place(x=500, y=200)
        self.intervals_button.place(x=100, y=300)
        self.dom_seventh_button.place(x=300, y=300)
        self.triads_button.place(x=500, y=300)
        self.start_button.place(x=300, y=400)

    # 0 - easy, 1 - medium, 2 - hard
    def change_mode(self, mode_number):
        self.current_mode.set(mode_number)
        prefix = "Current mode: "

        text = "EASY"
        if mode_number == 1:
            text = "MEDIUM"
        elif mode_number == 2:
            text = "HARD"

        self.mode_label['text'] = prefix + text

    def change_instrument(self, instrument_number):
        self.current_instrumnet.set(instrument_number)
        prefix = "Instrument picked: "

        text = "PIANO"
        if instrument_number == 1:
            text = "GUITAR"
        elif instrument_number == 2:
            text = "TRUMPET"

        self.instrument_label['text'] = prefix + text

    def change_ex_type(self, ex_number):

        self.current_ex_type.set(ex_number)
        prefix = "Exercise picked: "

        text = "INTERVALS"
        if ex_number == 1:
            text = "DOMINANT 7TH"
        elif ex_number == 2:
            text = "TRIADS"

        self.ex_type_label['text'] = prefix + text


    def tickbox_checked(self, button):
        pass


    def openNewWindow(self):

        # Toplevel object which will
        # be treated as a new window
        newWindow = Toplevel(initial)

        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")

        # sets the geometry of toplevel
        newWindow.geometry("700x500")

        # A Label widget to show in toplevel

        Label(newWindow,
              text="This is a new window").pack()


def main():
    App(initial)
    initial.mainloop()


if __name__ == "__main__":
    main()
