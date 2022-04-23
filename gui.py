import tkinter as tk
from windows.login_window import LoginWindow
from windows.exercise_window import ExerciseWindow
from windows.improvement_window import ImprovementWindow
from windows.info_window import InfoWindow
from windows.statistics_window import StatisticsWindow

from enum_types import Instrument, Mode, Exercise


# we can split different windows into different classes + modules or sth
class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()

        self.title("Ear Training App")
        self.geometry("850x600")
        self.wm_resizable(False, False)

        self.current_mode = Mode.EASY
        self.current_instrument = Instrument.PIANO
        self.current_exercise = Exercise.INTERVALS

        self.exercise_opened = False
        self.login_opened = False
        self.info_opened = False
        self.improvement_opened = False
        self.statistics_opened = False

        button_font = ('Comic Sans MS', 10, 'bold')
        instr_ex_mode_logged_font = ('Comic Sans MS', 12, 'bold italic')

        self.logged_label = tk.Label(
            text="You're not logged in - statistics will not be saved after closing!",
            font=instr_ex_mode_logged_font,
        )

        self.mode_label = tk.Label(
            text="Current mode: EASY",
            font=instr_ex_mode_logged_font,
        )

        self.instrument_label = tk.Label(
            text="Instrument picked: PIANO",
            font=instr_ex_mode_logged_font,
        )

        self.ex_type_label = tk.Label(
            text="Exercise picked: INTERVALS",
            font=instr_ex_mode_logged_font,
        )

        self.info_button = tk.Button(
            self,
            bg="pink",
            fg="white",
            width=22,
            text="Information about program",
            font=button_font,
            command=lambda: self.open_info_window()
        )

        self.login_button = tk.Button(
            self,
            bg="#B58B00",
            fg="white",
            width=15,
            text="Log in",
            font=button_font,
            command=lambda: self.open_login_window()
        )

        self.easy_button = tk.Button(
            self,
            bg="green",
            fg="white",
            width=15,
            text="EASY",
            font=button_font,
            command=lambda: self.change_mode(Mode.EASY)
        )

        self.medium_button = tk.Button(
            self,
            bg="green",
            fg="white",
            width=15,
            text="MEDIUM",
            font=button_font,
            command=lambda: self.change_mode(Mode.MEDIUM)
        )

        self.hard_button = tk.Button(
            self,
            bg="green",
            fg="white",
            width=15,
            text="HARD",
            font=button_font,
            command=lambda: self.change_mode(Mode.HARD)
        )

        self.piano_button = tk.Button(
            self,
            bg="purple",
            fg="white",
            width=15,
            text="Piano",
            font=button_font,
            command=lambda: self.change_instrument(Instrument.PIANO)
        )

        self.guitar_button = tk.Button(
            self,
            bg="purple",
            fg="white",
            width=15,
            text="Guitar",
            font=button_font,
            command=lambda: self.change_instrument(Instrument.GUITAR)
        )

        self.trumpet_button = tk.Button(
            self,
            bg="purple",
            fg="white",
            width=15,
            text="Trumpet",
            font=button_font,
            command=lambda: self.change_instrument(Instrument.TRUMPET)
        )

        self.intervals_button = tk.Button(
            self,
            bg="orange",
            fg="white",
            width=15,
            text="Intervals",
            font=button_font,
            command=lambda: self.change_ex_type(Exercise.INTERVALS)
        )

        self.triads_button = tk.Button(
            self,
            bg="orange",
            fg="white",
            width=15,
            text="Triads",
            font=button_font,
            command=lambda: self.change_ex_type(Exercise.TRIADS)
        )

        self.dom_seventh_button = tk.Button(
            self,
            bg="orange",
            fg="white",
            width=15,
            text="Dominant 7th",
            font=button_font,
            command=lambda: self.change_ex_type(Exercise.DOMINANT_7TH)
        )

        self.start_button = tk.Button(
            self,
            bg="red",
            fg="white",
            width=15,
            text="START!",
            font=button_font,
            command=lambda: self.open_exercise_window()
        )

        self.statistics_button = tk.Button(
            self,
            bg="blue",
            fg="white",
            width=15,
            text="Statistics",
            font=button_font,
            command=lambda: self.open_statistics_window()
        )

        self.improve_button = tk.Button(
            self,
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

        self.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.winfo_screenwidth() - 850) / 2
        y = (self.winfo_screenheight() - 700) / 2
        self.geometry("+%d+%d" % (x, y))

    # changing mode, instrument, ex_type
    def change_mode(self, mode: Mode):
        self.current_mode = mode
        self.mode_label['text'] = "Current mode: " + mode.name

    def change_instrument(self, instrument: Instrument):
        self.current_instrument = instrument
        self.instrument_label['text'] = "Instrument picked: " + instrument.name

    def change_ex_type(self, exercise: Exercise):
        self.current_exercise = exercise
        self.ex_type_label['text'] = "Exercise picked: " + "DOMINANT 7TH" if exercise == Exercise.DOMINANT_7TH else exercise.name

    # new windows
    def open_info_window(self):
        if not self.info_opened:
            info_window = InfoWindow(self)
            info_window.mainloop()

    def open_login_window(self):
        # TODO + csv + new window + change to log out
        if not self.login_opened:
            login_window = LoginWindow(self)
            login_window.mainloop()

    def open_improvement_window(self):
        # TODO
        if not self.improvement_opened:
            improvement_window = ImprovementWindow(self)
            improvement_window.mainloop()

    def open_statistics_window(self):
        # TODO
        if not self.statistics_opened:
            statistics_window = StatisticsWindow(self)
            statistics_window.mainloop()

    def open_exercise_window(self):
        if not self.exercise_opened:
            exercise_window = ExerciseWindow(self, self.current_instrument, self.current_exercise)
            exercise_window.mainloop()


def main():
    App().mainloop()


if __name__ == "__main__":
    main()

# language, password + user - password, user w csv ewentualnie chronione hasłem
# kalendarzyk może idk
# ask about repetition in windows classes
