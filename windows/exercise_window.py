import tkinter as tk
from enum_types import Instrument, Mode, Exercise
from .base_window import BaseWindow
import sys
sys.path.append("..")
from exercise_handler import ExerciseHandler

class ExerciseWindow(BaseWindow):

    def __init__(self, master_root, instrument, exercise):
        super().__init__(master_root, 850, 700, "Exercise")
        self.instrument_used = instrument
        self.exercise_used = exercise
        harmonics_label = tk.Label(
            self,
            text="Choose mode: ",
            font=('Comic Sans MS', 18, 'bold italic'),
        )

        if instrument != Instrument.TRUMPET:
            available_harmonics = ['melodycznie - w górę', 'melodycznie - w dół', 'harmonicznie',
                                   'melodycznie w górę + harmonicznie', 'melodycznie w dół + harmonicznie']
        else:
            available_harmonics = ['melodycznie - w górę', 'melodycznie - w dół']

        self.variable = tk.StringVar()
        self.variable.set(available_harmonics[0])

        self.dropdown = tk.OptionMenu(
            self,
            self.variable,
            *available_harmonics,
        )

        # TODO - idk co tu chciałaś
        self.dropdown['menu'].config(font=('Comic Sans MS', 12, 'bold'))

        harmonics_label.place(x=350, y=20)
        self.dropdown.place(x=350, y=70)

        if exercise == Exercise.INTERVALS:
            self.what_to_play = [tk.BooleanVar() for _ in range(13)]
            self.names = ['Pryma 1', 'Sekunda mała 2>', 'Sekundka wielka 2', 'Tercja mała 3>', 'Tercja wielka 3',
                               'Kwarta czysta 4', 'Tryton 4</5>', 'Kwinta czysta 5', 'Seksta mała 6>',' Seksta wielka 6',
                               'Septyma mała 7', 'Septyma wielka 7<', 'Oktawa']

            infix = "intervals "

        elif exercise == Exercise.DOMINANT_7TH:
            self.what_to_play = [tk.BooleanVar() for _ in range(4)]
            self.names = ['Zasadnicza', 'I przewrót', 'II przewrót', 'III przewrót']

            infix = "dominants "

        else:
            self.what_to_play = [tk.BooleanVar() for _ in range(10)]
            self.names = ['Durowy zasadniczy', 'Durowy sekstowy', 'Durowy kwartsekstowy', 'Molowy zasadniczy',
                            'Molowy sekstowy', 'Molowy kwartsekstowy', 'Zmniejszony zasadniczy', 'Zmniejszony sekstowy',
                            'Zmniejszony kwartsekstowy', 'Zwiększony kwartsekstowy']

            infix = "triads "

        self.check_buttons = [
            tk.Checkbutton(self, text=self.names[i], variable=self.what_to_play[i], onvalue=True,
                           offvalue=False, font=('Comic Sans MS', 15, 'bold')) for i in range(len(self.what_to_play))]

        # do it in all cases
        instruction_label = tk.Label(
            self,
            text="Uncheck " + infix + "you don't want to train",
            font=('Comic Sans MS', 18, 'bold italic'),
        )

        instruction_label.place(x=450, y=130, anchor="center")

        for i in range(len(self.check_buttons)):
            self.check_buttons[i].select()
            self.check_buttons[i].place(x=350, y=160 + i * 35)

        start_button = tk.Button(
            self,
            bg="red",
            fg="white",
            width=15,
            text="START!",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.start_exercising()
        )

        start_button.place(x=350, y=630)


    def start_exercising(self):
        start_ex_window = tk.Toplevel(self)
        start_ex_window.title("Ćwiczenie")
        start_ex_window.geometry("850x700")

        self.exercise_handler = ExerciseHandler(self.instrument_used, self.exercise_used, self.variable.get(), self.what_to_play)
        buttons_list = []
        j = 0
        for i in range (0, len(self.names), 1):
            if (self.what_to_play[i].get() == True):
                buttons_list.append(tk.Button(
                start_ex_window,
                bg="blue",
                fg="white",
                width=15,
                text=self.names[i],
                font=('Comic Sans MS', 10, 'bold'),
                command=lambda: self.exercise_handler.check_accuracy
                ))
                buttons_list[j].place(x = 350, y = 40 + j * 40)
                j += 1

        next_button = tk.Button(
            start_ex_window,
            bg="red",
            text = "NEXT",
            fg="orange",
            width=15,
            font=('Comic Sans MS', 10, 'bold'),
            command = lambda:  self.exercise_handler.next_sound()
        )



        repeat_button = tk.Button(
            start_ex_window,
            bg="red",
            fg="orange",
            text = "REPEAT",
            width=15,
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda:  self.exercise_handler.repeat_sound()
        )

        next_button.place(x=530, y=600)
        repeat_button.place(x = 670, y = 600)
        start_ex_window.mainloop()



