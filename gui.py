import tkinter as tk

from options_frame import OptionsFrame
from windows.login_window import LoginWindow
from windows.choose_exercise_window import ChooseExerciseWindow
from windows.improvement_window import ImprovementWindow
from windows.info_window import InfoWindow
from windows.statistics_window import StatisticsWindow

from enum_types import Instrument, Mode, Exercise


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ear Training App")
        self.geometry("850x600")
        self.wm_resizable(False, False)

        self.current_mode = Mode.EASY
        self.current_instrument = Instrument.PIANO
        self.current_exercise = Exercise.INTERVALS

        self.choose_exercise_opened = False
        self.login_opened = False
        self.info_opened = False
        self.improvement_opened = False
        self.statistics_opened = False

        self.logged_user = None

        button_font = ('Comic Sans MS', 10, 'bold')
        instr_ex_mode_logged_font = ('Comic Sans MS', 12, 'bold italic')

        self.main_frame = OptionsFrame(self)
        self.main_frame.place(x=150, y=175)

        self.logged_label = tk.Label(
            text="You're not logged in - statistics will not be saved after closing!",
            font=instr_ex_mode_logged_font,
        )

        self.info_button = tk.Button(
            self,
            bg="pink",
            fg="white",
            width=25,
            text="Information about the program",
            font=button_font,
            command=self.open_info_window
        )

        self.log_in_button = tk.Button(
            self,
            bg="#B58B00",
            fg="white",
            width=15,
            text="Log in",
            font=button_font,
            command=self.open_login_window
        )

        self.start_button = tk.Button(
            self,
            bg="red",
            fg="white",
            width=15,
            text="START!",
            font=button_font,
            command=self.open_exercise_window
        )

        self.statistics_button = tk.Button(
            self,
            bg="blue",
            fg="white",
            width=15,
            text="Statistics",
            font=button_font,
            command=self.open_statistics_window
        )

        self.improve_button = tk.Button(
            self,
            bg="blue",
            fg="white",
            width=16,
            text="Areas to improve in",
            font=button_font,
            command=self.open_improvement_window
        )

        self.info_button.place(x=320, y=15)
        self.logged_label.place(x=420, y=75, anchor="center")
        self.log_in_button.place(x=350, y=100)
        self.start_button.place(x=350, y=500)
        self.statistics_button.place(x=50, y=550)
        self.improve_button.place(x=670, y=550)

        self.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.winfo_screenwidth() - 850) / 2
        y = (self.winfo_screenheight() - 700) / 2
        self.geometry("+%d+%d" % (x, y))

    def log_out(self):
        self.log_in_button['text'] = "Log in"
        self.log_in_button['command'] = self.open_login_window
        self.logged_label['text'] = "You're not logged in - statistics will not be saved after closing!"
        self.logged_user = None

    # new windows
    def open_info_window(self):
        if not self.info_opened:
            info_window = InfoWindow(self)
            info_window.mainloop()

    def open_login_window(self):
        if not self.login_opened:
            login_window = LoginWindow(self)
            login_window.mainloop()

    def open_improvement_window(self):
        if not self.improvement_opened:
            improvement_window = ImprovementWindow(self)
            improvement_window.mainloop()

    def open_statistics_window(self):
        if not self.statistics_opened:
            statistics_window = StatisticsWindow(self)
            statistics_window.mainloop()

    def open_exercise_window(self):
        if not self.choose_exercise_opened:
            choose_exercise_window = ChooseExerciseWindow(self, self.current_instrument, self.current_exercise, self.current_mode)
            choose_exercise_window.mainloop()


def main():
    App().mainloop()


if __name__ == "__main__":
    main()

# TODO list:
#  jednolitość języka!!!
#  streak, top scores, areas to improve (improve)
#  rozwiązanie wielokrotnego otwierania pliku csv - trzymać w pamięci i na końcu zapisać, może baza danych? idk
#  SKRYPT FFMPEG NA RÓŻNE POZIOMY TRUDNOŚCI, BĘDZIE ON 10 LAT SZEDŁ WIĘC TRZEBA NAPISAĆ DOBRZE
