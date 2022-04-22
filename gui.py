import tkinter as tk
from login_window import LoginWindow
from exercise_windows import ExerciseWindow
from enum_types import Instrument, Mode, Exercise


# we can split different windows into different classes + modules or sth
class App:
    def __init__(self, root):
        self.root = root

        self.current_mode = Mode.EASY
        self.current_instrument = Instrument.PIANO
        self.current_exercise = Exercise.INTERVALS

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
            command=lambda: self.change_mode(Mode.EASY)
        )

        self.medium_button = tk.Button(
            root,
            bg="green",
            fg="white",
            width=15,
            text="MEDIUM",
            font=button_font,
            command=lambda: self.change_mode(Mode.MEDIUM)
        )

        self.hard_button = tk.Button(
            root,
            bg="green",
            fg="white",
            width=15,
            text="HARD",
            font=button_font,
            command=lambda: self.change_mode(Mode.HARD)
        )

        self.piano_button = tk.Button(
            root,
            bg="purple",
            fg="white",
            width=15,
            text="Piano",
            font=button_font,
            command=lambda: self.change_instrument(Instrument.PIANO)
        )

        self.guitar_button = tk.Button(
            root,
            bg="purple",
            fg="white",
            width=15,
            text="Guitar",
            font=button_font,
            command=lambda: self.change_instrument(Instrument.GUITAR)
        )

        self.trumpet_button = tk.Button(
            root,
            bg="purple",
            fg="white",
            width=15,
            text="Trumpet",
            font=button_font,
            command=lambda: self.change_instrument(Instrument.TRUMPET)
        )

        self.intervals_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Intervals",
            font=button_font,
            command=lambda: self.change_ex_type(Exercise.INTERVALS)
        )

        self.triads_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Triads",
            font=button_font,
            command=lambda: self.change_ex_type(Exercise.TRIADS)
        )

        self.dom_seventh_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Dominant 7th",
            font=button_font,
            command=lambda: self.change_ex_type(Exercise.DOMINANT_7TH)
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

    def change_mode(self, mode: Mode):
        self.current_mode = mode
        self.mode_label['text'] = "Current mode: " + mode.name

    def change_instrument(self, instrument: Instrument):
        self.current_instrument = instrument
        self.instrument_label['text'] = "Instrument picked: " + instrument.name

    def change_ex_type(self, exercise: Exercise):
        self.current_exercise = exercise
        self.ex_type_label['text'] = "Exercise picked: " + "DOMINANT 7TH" if exercise == Exercise.DOMINANT_7TH else exercise.name

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
        # TODO
        improvement_window = tk.Toplevel(self.root)
        improvement_window.wm_resizable(False, False)
        improvement_window.title("Areas to improve")
        improvement_window.geometry("850x600")
        improvement_window.mainloop()

    def open_statistics_window(self):
        # TODO
        statistics_window = tk.Toplevel(self.root)
        statistics_window.wm_resizable(False, False)
        statistics_window.title("Statistics")
        statistics_window.geometry("850x600")
        statistics_window.mainloop()

    def open_exercise_window(self):
        exercise_window = ExerciseWindow(self.root, self.current_instrument, self.current_exercise)
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
# kalendarzyk może idk
# niemożliwość klikania na wcześniejszy ekran milion razy - TODO
