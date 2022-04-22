import tkinter as tk

# Frame TODO
class mode_picker:

    def __init__(self):


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

