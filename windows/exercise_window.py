import tkinter as tk

from enum_types import Exercise
from .base_window import BaseWindow
from .exercise_handler import ExerciseHandler


class ExerciseWindow(BaseWindow):
    def __init__(self, master_root, width, height, title, instrument, exercise, names, harmonics, what_to_play, mode):
        super().__init__(master_root, width, height, title)

        self.exercise_handler = ExerciseHandler(self, instrument, exercise, harmonics, what_to_play, mode)
        buttons_list = []

        self.correctness_label = tk.Label(self, font=('Comic Sans MS', 10, 'bold'))
        self.correctness_label.place(x=100, y=600)

        j = 0
        width = 15 if exercise != Exercise.TRIADS else 22
        for i in range(len(names)):
            if what_to_play[i].get():
                buttons_list.append(tk.Button(
                    self,
                    bg="blue",
                    fg="white",
                    width=width,
                    text=names[i],
                    font=('Comic Sans MS', 10, 'bold'),
                    command=self.exercise_handler.check_accuracy_outer(i)
                    # https://stackoverflow.com/questions/45134097/deep-copy-index-integer-using-lambda
                ))
                buttons_list[j].place(x=350, y=40 + j * 40)
                j += 1

        next_button = tk.Button(
            self,
            bg="red",
            text="NEXT",
            fg="orange",
            width=15,
            font=('Comic Sans MS', 10, 'bold'),
            command=self.exercise_handler.next_sound
        )

        repeat_button = tk.Button(
            self,
            bg="red",
            fg="orange",
            text="REPEAT",
            width=15,
            font=('Comic Sans MS', 10, 'bold'),
            command=self.exercise_handler.repeat_sound
        )

        next_button.place(x=530, y=600)
        repeat_button.place(x=670, y=600)

    def destroy(self):
        self.exercise_handler.destroy()
        super().destroy()

    def set_opened(self, val):
        self.master_root.exercise_window_opened = val
