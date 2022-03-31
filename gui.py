import tkinter as tk


# we can split different windows into different clasees + modules or sth
class App:
    def __init__(self, root):
        self.root = root

        self.current_mode = tk.IntVar()

        self.mode_label = tk.Label(
            text="Current mode: EASY",
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

        self.intervals_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Intervals",
            font=('Comic Sans MS', 10, 'bold'),
        )

        self.triads_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Triads",
            font=('Comic Sans MS', 10, 'bold'),
        )

        self.mode_label.place(x=350 - 80, y=20)
        self.easy_button.place(x=100, y=100)
        self.medium_button.place(x=300, y=100)
        self.hard_button.place(x=500, y=100)
        self.intervals_button.place(x=150, y=200)
        self.triads_button.place(x=450, y=200)

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


def main():
    initial = tk.Tk()
    initial.geometry("700x500")
    initial.wm_resizable(False, False)
    App(initial)
    initial.mainloop()


if __name__ == "__main__":
    main()
