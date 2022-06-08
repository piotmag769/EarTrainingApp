import tkinter as tk

from enum_types import Mode, Instrument, Exercise


class OptionsFrame(tk.Frame):
    def __init__(self, master_root):
        super().__init__(master_root, height=290, width=530)

        self.master_root = master_root

        button_font = ('Comic Sans MS', 10, 'bold')
        instr_ex_mode_logged_font = ('Comic Sans MS', 12, 'bold italic')

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

        self.mode_label = tk.Label(
            self,
            text="Current mode: EASY",
            font=instr_ex_mode_logged_font,
        )

        self.instrument_label = tk.Label(
            self,
            text="Instrument picked: GUITAR",
            font=instr_ex_mode_logged_font,
        )

        self.ex_type_label = tk.Label(
            self,
            text="Exercise picked: INTERVALS",
            font=instr_ex_mode_logged_font,
        )

        self.mode_label.place(x=270, y=225, anchor="center")
        self.instrument_label.place(x=270, y=250, anchor="center")
        self.ex_type_label.place(x=270, y=275, anchor="center")
        self.easy_button.place(x=0, y=0)
        self.medium_button.place(x=200, y=0)
        self.hard_button.place(x=400, y=0)
        self.piano_button.place(x=0, y=75)
        self.guitar_button.place(x=200, y=75)
        self.trumpet_button.place(x=400, y=75)
        self.intervals_button.place(x=0, y=150)
        self.dom_seventh_button.place(x=200, y=150)
        self.triads_button.place(x=400, y=150)

    def change_mode(self, mode: Mode):
        self.master_root.current_mode = mode
        self.mode_label['text'] = "Current mode: " + mode.name

    def change_instrument(self, instrument: Instrument):
        self.master_root.current_instrument = instrument
        self.instrument_label['text'] = "Instrument picked: " + instrument.name

    def change_ex_type(self, exercise: Exercise):
        self.master_root.current_exercise = exercise
        self.ex_type_label['text'] = "Exercise picked: " + (
            "DOMINANT 7TH" if exercise == Exercise.DOMINANT_7TH else exercise.name)
