import tkinter as tk
from login_window import LoginWindow


# we can split different windows into different classes + modules or sth
class App:
    def __init__(self, root):
        self.root = root

        self.current_mode = tk.IntVar()
        self.current_instrument = tk.IntVar()
        self.current_ex_type = tk.IntVar()

        button_font = ('Comic Sans MS', 10, 'bold')

        self.logged_label = tk.Label(
            text="You're not logged in - statistics will not be saved after closing!",
            font=('Comic Sans MS', 12, 'bold italic'),
        )

        self.mode_label = tk.Label(
            text="Current mode: EASY",
            font=('Comic Sans MS', 12, 'bold italic'),
        )

        self.instrument_label = tk.Label(
            text="Instrument picked: PIANO",
            font=('Comic Sans MS', 12, 'bold italic'),
        )

        self.ex_type_label = tk.Label(
            text="Exercise picked: INTERVALS",
            font=('Comic Sans MS', 12, 'bold italic'),
        )

        self.info_button = tk.Button(
            root,
            bg="pink",
            fg="white",
            width=22,
            text="Information about program",
            font=button_font,
            command=lambda: self.open_program_info_window()
        )

        self.login_button = tk.Button(
            root,
            bg="#B58B00",
            fg="white",
            width=15,
            text="Log in",
            font=button_font,
            command=lambda: self.open_login_window()
        )

        self.easy_button = tk.Button(
            root,
            bg="green",
            fg="white",
            width=15,
            text="EASY",
            font=button_font,
            command=lambda: self.change_mode(0)
        )

        self.medium_button = tk.Button(
            root,
            bg="green",
            fg="white",
            width=15,
            text="MEDIUM",
            font=button_font,
            command=lambda: self.change_mode(1)
        )

        self.hard_button = tk.Button(
            root,
            bg="green",
            fg="white",
            width=15,
            text="HARD",
            font=button_font,
            command=lambda: self.change_mode(2)
        )

        self.piano_button = tk.Button(
            root,
            bg="purple",
            fg="white",
            width=15,
            text="Piano",
            font=button_font,
            command=lambda: self.change_instrument(0)
        )

        self.guitar_button = tk.Button(
            root,
            bg="purple",
            fg="white",
            width=15,
            text="Guitar",
            font=button_font,
            command=lambda: self.change_instrument(1)
        )

        self.trumpet_button = tk.Button(
            root,
            bg="purple",
            fg="white",
            width=15,
            text="Trumpet",
            font=button_font,
            command=lambda: self.change_instrument(2)
        )

        self.intervals_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Intervals",
            font=button_font,
            command=lambda: self.change_ex_type(0)
        )

        self.triads_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Triads",
            font=button_font,
            command=lambda: self.change_ex_type(2)
        )

        self.dom_seventh_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Dominant 7th",
            font=button_font,
            command=lambda: self.change_ex_type(1)
        )

        self.start_button = tk.Button(
            root,
            bg="red",
            fg="white",
            width=15,
            text="START!",
            font=button_font,
            command=lambda: self.open_exercise_window()
        )

        self.statistics_button = tk.Button(
            root,
            bg="blue",
            fg="white",
            width=15,
            text="Statistics",
            font=button_font,
            command=lambda: self.open_statistics_window()
        )

        self.improve_button = tk.Button(
            root,
            bg="blue",
            fg="white",
            width=15,
            text="Areas to improve in",
            font=button_font,
            command=lambda: self.open_improvement_window()
        )

        self.info_button.place(x=327.5, y=15)
        self.logged_label.place(x=420, y=75, anchor="center")
        self.mode_label.place(x=420, y=400, anchor="center")
        self.instrument_label.place(x=420, y=425, anchor="center")
        self.ex_type_label.place(x=420, y=450, anchor="center")
        self.login_button.place(x=350, y=100)
        self.easy_button.place(x=150, y=175)
        self.medium_button.place(x=350, y=175)
        self.hard_button.place(x=550, y=175)
        self.piano_button.place(x=150, y=250)
        self.guitar_button.place(x=350, y=250)
        self.trumpet_button.place(x=550, y=250)
        self.intervals_button.place(x=150, y=325)
        self.dom_seventh_button.place(x=350, y=325)
        self.triads_button.place(x=550, y=325)
        self.start_button.place(x=350, y=500)
        self.statistics_button.place(x=50, y=550)
        self.improve_button.place(x=670, y=550)

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
        self.current_instrument.set(instrument_number)
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

    def open_program_info_window(self):
        # TODO
        info_window = tk.Toplevel(self.root)
        info_window.wm_resizable(False, False)
        info_window.title("Information about program")
        info_window.geometry("850x600")
        info_window.mainloop()

    def open_login_window(self):
        # TODO + csv + new window + change to log out
        login_window = LoginWindow(self.root)
        login_window.mainloop()

    def open_improvement_window(self):
        improvement_window = tk.Toplevel(self.root)
        improvement_window.wm_resizable(False, False)
        improvement_window.title("Areas to improve")
        improvement_window.geometry("850x600")
        improvement_window.mainloop()

    def open_statistics_window(self):
        statistics_window = tk.Toplevel(self.root)
        statistics_window.wm_resizable(False, False)
        statistics_window.title("Statistics")
        statistics_window.geometry("850x600")
        statistics_window.mainloop()

    def open_exercise_window(self):
        exercise_window = tk.Toplevel(self.root)
        exercise_window.wm_resizable(False, False)
        exercise_window.title("Exercise")
        exercise_window.geometry("850x700")

        harmonics_label = tk.Label(
            exercise_window,
            text="Choose mode: ",
            font=('Comic Sans MS', 18, 'bold italic'),
        )

        if self.current_instrument.get() == 0 or self.current_instrument.get() == 1:
            available_harmonics = ['melodycznie - w górę', 'melodycznie - w dół', 'harmonicznie',
                                   'melodycznie w górę + harmonicznie', 'melodycznie w dół + harmonicznie']
        else:
            available_harmonics = ['melodycznie - w górę', 'melodycznie - w dół']

        variable = tk.StringVar()
        variable.set(available_harmonics[0])

        dropdown = tk.OptionMenu(
            exercise_window,
            variable,
            *available_harmonics,
        )

        # TODO
        dropdown['menu'].config(font=('Comic Sans MS', 12, 'bold'))

        harmonics_label.place(x=350, y=20)
        dropdown.place(x=350, y=70)

        if self.current_ex_type.get() == 0:
            what_to_play = [tk.BooleanVar() for _ in range(13)]
            intervals_names = ['Pryma 1', 'Sekunda mała 2>', 'Sekundka wielka 2', 'Tercja mała 3>', 'Tercja wielka 3',
                               'Kwarta czysta 4', 'Tryton 4</5>', 'Kwinta czysta 5', 'Seksta mała 6>',' Seksta wielka 6',
                               'Septyma mała 7', 'Septyma wielka 7<', 'Oktawa']

            check_buttons = [
                tk.Checkbutton(exercise_window, text=intervals_names[i], variable=what_to_play[i], onvalue=True,
                               offvalue=False, font=('Comic Sans MS', 15, 'bold')) for i in range(13)]

            infix = "intervals "

        elif self.current_ex_type.get() == 1:
            what_to_play = [tk.BooleanVar() for _ in range(4)]
            dominants_names = ['Zasadnicza', 'I przewrót', 'II przewrót', 'III przewrót']

            check_buttons = [
                tk.Checkbutton(exercise_window, text=dominants_names[i], variable=what_to_play[i], onvalue=True,
                               offvalue=False, font=('Comic Sans MS', 15, 'bold')) for i in range(4)]

            infix = "dominants "

        else:
            what_to_play = [tk.BooleanVar() for _ in range(10)]
            triads_names = ['Durowy zasadniczy', 'Durowy sekstowy', 'Durowy kwartsekstowy', 'Molowy zasadniczy',
                            'Molowy sekstowy', 'Molowy kwartsekstowy', 'Zmniejszony zasadniczy', 'Zmniejszony sekstowy',
                            'Zmniejszony kwartsekstowy', 'Zwiększony kwartsekstowy']

            check_buttons = [
                tk.Checkbutton(exercise_window, text=triads_names[i], variable=what_to_play[i], onvalue=True,
                               offvalue=False, font=('Comic Sans MS', 15, 'bold')) for i in range(10)]

            infix = "triads "

        # do it in all cases
        instruction_label = tk.Label(
            exercise_window,
            text="Uncheck " + infix + "you don't want to train",
            font=('Comic Sans MS', 18, 'bold italic'),
        )

        instruction_label.place(x=450, y=130, anchor="center")

        for i in range(len(check_buttons)):
            check_buttons[i].select()
            check_buttons[i].place(x=350, y=160 + i * 35)

##########################################

        exercise_start_button = tk.Button(
            exercise_window,
            bg="red",
            fg="white",
            width=15,
            text="START!",
            font=('Comic Sans MS', 10, 'bold'),
        )

        exercise_start_button.place(x=350, y=630)

        exercise_window.update_idletasks()  # Update "requested size" from geometry manager

        x = (exercise_window.winfo_screenwidth() - 850) / 2
        y = (exercise_window.winfo_screenheight() - 700) / 2
        exercise_window.geometry("+%d+%d" % (x, y))

        exercise_window.mainloop()


def main():
    initial = tk.Tk()
    initial.title("Ear Training App")
    initial.geometry("850x600")
    initial.wm_resizable(False, False)
    App(initial)
    initial.mainloop()


if __name__ == "__main__":
    main()

# language, password + user - password, user w csv ewentualnie chronione hasłem
# button obok checkboxa w starcie
# kalendarzyk może idk
# niemożliwość klikania na wcześniejszy ekran milion razy
