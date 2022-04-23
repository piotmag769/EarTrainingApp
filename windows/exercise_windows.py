import tkinter as tk
from enum_types import Instrument, Mode, Exercise


class ExerciseWindow(tk.Toplevel):
    def __init__(self, master_root, instrument, exercise, already_opened):

        if already_opened:
            super().destroy()
            return

        super().__init__(master_root)
        self.wm_resizable(False, False)
        self.title("Exercise")
        self.geometry("850x700")

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

        variable = tk.StringVar()
        variable.set(available_harmonics[0])

        dropdown = tk.OptionMenu(
            self,
            variable,
            *available_harmonics,
        )

        # TODO - idk co tu chciałaś
        dropdown['menu'].config(font=('Comic Sans MS', 12, 'bold'))

        harmonics_label.place(x=350, y=20)
        dropdown.place(x=350, y=70)

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
        )

        start_button.place(x=350, y=630)

        self.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.winfo_screenwidth() - 850) / 2
        y = (self.winfo_screenheight() - 700) / 2
        self.geometry("+%d+%d" % (x, y))

        # TODO buttons - button obok checkboxa w starcie

        self.master_root = master_root
        self.master_root.exercise_opened = True

    def destroy(self):
        self.master_root.exercise_opened = False
        super().destroy()
