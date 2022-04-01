import tkinter as tk
from tkinter import *
from tkinter.ttk import *


initial = tk.Tk()
initial.title("Ear Training - welcome")
initial.geometry("850x600")
initial.wm_resizable(False, False)

# we can split different windows into different classes + modules or sth
class App:
    def __init__(self, root):
        self.root = root

        self.current_mode = tk.IntVar()
        self.current_instrument = tk.IntVar()
        self.current_ex_type = tk.IntVar()


        self.logged_label = tk.Label(
            text="You're not logged in; statistics will not be saved after closing",
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
            text = "Exercise picked: INTERVALS",
            font=('Comic Sans MS', 12, 'bold italic'),
        )

        self.info_button = tk.Button(
            root,
            bg="pink",
            fg="white",
            width=20,
            text="Informacje o programie",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.open_program_info_window()
        )


        self.login_button = tk.Button(
            root,
            bg="yellow",
            fg="white",
            width=15,
            text="Log in",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.open_login_window()
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

        self.piano_button = tk.Button(
            root,
            bg="purple",
            fg="white",
            width=15,
            text="Piano",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_instrument(0)
        )

        self.guitar_button = tk.Button(
            root,
            bg="purple",
            fg="white",
            width=15,
            text="Guitar",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_instrument(1)
        )

        self.trumpet_button = tk.Button(
            root,
            bg="purple",
            fg="white",
            width=15,
            text="Trumpet",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_instrument(2)
        )

        self.intervals_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Intervals",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_ex_type(0)
        )

        self.triads_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Triads",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_ex_type(2)
        )

        self.dom_seventh_button = tk.Button(
            root,
            bg="orange",
            fg="white",
            width=15,
            text="Dominant 7th",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.change_ex_type(1)
        )

        self.start_button = tk.Button(
            root,
            bg="red",
            fg="white",
            width=15,
            text="START!",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.open_exercise_window()

        )

        self.statistics_button = tk.Button(
            root,
            bg="blue",
            fg="white",
            width=15,
            text="Statistics",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.open_statistics_window()

        )

        self.improve_button = tk.Button(
            root,
            bg="blue",
            fg="white",
            width=15,
            text="Areas to improve in",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.open_improvement_window()

        )

        self.info_button.place(x = 327.5, y = 15)
        self.logged_label.place(x = 420, y = 75, anchor="center")
        self.mode_label.place(x=420, y=400, anchor="center")
        self.instrument_label.place(x = 420, y=425, anchor="center")
        self.ex_type_label.place(x = 420, y = 450, anchor="center")
        self.login_button.place(x = 350, y = 100)
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
        self.statistics_button.place(x = 50, y = 550)
        self.improve_button.place(x = 670, y = 550)

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
        info_window = Toplevel(initial)
        info_window.title("Informacje o programie")
        info_window.geometry("850x600")
        info_window.mainloop()

    def open_login_window(self):

        login_window = Toplevel(initial)
        login_window.title("Logowanie")
        login_window.geometry("850x600")
        username_label = tk.Label(login_window,
                                       text="username:",
                                       font=('Comic Sans MS', 15),
                                       )
        password_label = tk.Label(login_window,
                                  text="password:",
                                  font=('Comic Sans MS',   15),
                                  )
        no_account_label = tk.Label(login_window,
                                  text="No account?",
                                  font=('Comic Sans MS', 18),
                                  )
        username_input = tk.Entry(login_window, font=('Comic Sans MS', 10))
        password_input = tk.Entry(login_window, show="*", font=('Comic Sans MS', 10))
        login_button = tk.Button(
            login_window,
            bg="blue",
            fg="white",
            width=15,
            text="Login",
            font=('Comic Sans MS', 10, 'bold')
        )
        new_account_button = tk.Button(
            login_window,
            bg="pink",
            fg="black",
            width=20,
            text="Create a new account!",
            font=('Comic Sans MS', 10, 'bold')
        )
        username_label.place(x = 300, y = 50)
        password_label.place(x = 300, y = 100)
        username_input.place(x = 400, y = 50)
        password_input.place(x = 400, y = 100)
        login_button.place(x = 360, y = 150)
        no_account_label.place(x = 420, y = 250, anchor="center")
        new_account_button.place(x = 340, y = 300)
        login_window.mainloop()


    def open_improvement_window(self):

        improvement_window = Toplevel(initial)
        improvement_window.title("Areas to improve")
        improvement_window.geometry("850x600")
        improvement_window.mainloop()

    def open_statistics_window(self):

        statistics_window = Toplevel(initial)
        statistics_window.title("Statystyki")
        statistics_window.geometry("850x600")
        statistics_window.mainloop()

    def open_exercise_window(self):


        exercise_window = Toplevel(initial)
        exercise_window.title("Ćwiczenie")
        exercise_window.geometry("850x700")

        harmonics_label = tk.Label(exercise_window,
                                   text="Wybierz tryb: ",
                                   font=('Comic Sans MS', 18, 'bold italic'),
                                   )
        if self.current_instrument.get() == 0 or self.current_instrument.get() == 1:
            available_harmonics = ['melodycznie - w górę', 'melodycznie - w dół', 'harmonicznie',
                                   'melodycznie w górę + harmonicznie', 'melodycznie w doł + harmonicznie']
        else:
            available_harmonics = ['melodycznie - w górę', 'melodycznie - w dół']

        variable = StringVar()
        variable.set(available_harmonics[0])
        dropdown = OptionMenu(
            exercise_window,
            variable,
            *available_harmonics,
        )
        dropdown['menu'].config(font=('Comic Sans MS', 12, 'bold'))
        harmonics_label.place(x = 350, y = 20)
        dropdown.place(x = 350, y = 70)

        if self.current_ex_type.get() == 0:
            v1 = IntVar
            c1 = tk.Checkbutton(exercise_window, text='Pryma 1',variable=v1, onvalue=1, offvalue=0,
            font=('Comic Sans MS', 15, 'bold'))
            v2 = IntVar
            c2 = tk.Checkbutton(exercise_window, text='Sekunda mała 2>', variable=v2, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v3 = IntVar
            c3 = tk.Checkbutton(exercise_window, text='Sekunda wielka 2',variable=v3, onvalue=1, offvalue=0,
            font=('Comic Sans MS', 15, 'bold'))
            v4 = IntVar
            c4 = tk.Checkbutton(exercise_window, text='Tercja mała 3>', variable=v4, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v5 = IntVar
            c5 = tk.Checkbutton(exercise_window, text='Tercja wielka 3', variable=v5, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v6 = IntVar
            c6 = tk.Checkbutton(exercise_window, text='Kwarta czysta 4', variable=v6, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v7 = IntVar
            c7 = tk.Checkbutton(exercise_window, text='Tryton 4</5>', variable=v7, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v8 = IntVar
            c8 = tk.Checkbutton(exercise_window, text='Kwinta czysta 5', variable=v8, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v9 = IntVar
            c9 = tk.Checkbutton(exercise_window, text='Seksta mała 6>', variable=v9, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v10 = IntVar
            c10 = tk.Checkbutton(exercise_window, text='Seksta wielka 6', variable=v10, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v11 = IntVar
            c11 = tk.Checkbutton(exercise_window, text='Septyma mała 7', variable=v11, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v12 = IntVar
            c12 = tk.Checkbutton(exercise_window, text='Septyma wielka 7<', variable=v12, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v13 = IntVar
            c13 = tk.Checkbutton(exercise_window, text='Oktawa', variable=v13, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))

            intervals_label = tk.Label(exercise_window,
                text="Odznacz interwały, których nie chcesz słuchać",
                font=('Comic Sans MS', 18, 'bold italic'),
            )
            intervals_label.place(x = 450, y = 130, anchor="center")
            c1.select()
            c2.select()
            c3.select()
            c4.select()
            c5.select()
            c6.select()
            c7.select()
            c8.select()
            c9.select()
            c10.select()
            c11.select()
            c12.select()
            c13.select()
            c1.place(x = 350, y = 160)
            c2.place(x=350, y=190)
            c3.place(x=350, y=220)
            c4.place(x=350, y=250)
            c5.place(x=350, y=280)
            c6.place(x=350, y=310)
            c7.place(x=350, y=340)
            c8.place(x=350, y=370)
            c9.place(x=350, y=400)
            c10.place(x=350, y=430)
            c11.place(x=350, y=460)
            c12.place(x=350, y=490)
            c13.place(x=350, y=520)

            #interwały
        elif self.current_ex_type.get() == 1:
            v1 = IntVar
            c1 = tk.Checkbutton(exercise_window, text='Zasadnicza', variable=v1, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v2 = IntVar
            c2 = tk.Checkbutton(exercise_window, text='I przewrót', variable=v2, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v3 = IntVar
            c3 = tk.Checkbutton(exercise_window, text='II przewrót', variable=v3, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v4 = IntVar
            c4 = tk.Checkbutton(exercise_window, text='III przewrót', variable=v4, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            dominant_label = tk.Label(exercise_window,
                                       text="Odznacz postacie dominanty, których nie chcesz słuchać",
                                       font=('Comic Sans MS', 18, 'bold italic'),
                                       )
            dominant_label.place(x=450, y=130, anchor="center")
            c1.place(x=350, y=160)
            c2.place(x=350, y=190)
            c3.place(x=350, y=220)
            c4.place(x=350, y=250)
            c1.select()
            c2.select()
            c3.select()
            c4.select()
        #dominanta

        else:
            v1 = IntVar
            c1 = tk.Checkbutton(exercise_window, text='Durowy zasadniczy', variable=v1, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v2 = IntVar
            c2 = tk.Checkbutton(exercise_window, text='Durowy sekstowy', variable=v2, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v3 = IntVar
            c3 = tk.Checkbutton(exercise_window, text='Durowy kwartsekstowy', variable=v3, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v4 = IntVar
            c4 = tk.Checkbutton(exercise_window, text='Molowy zasadniczy', variable=v4, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v5 = IntVar
            c5 = tk.Checkbutton(exercise_window, text='Molowy sekstowy', variable=v5, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v6 = IntVar
            c6 = tk.Checkbutton(exercise_window, text='Molowy kwartsekstowy', variable=v6, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v4 = IntVar
            c4 = tk.Checkbutton(exercise_window, text='Molowy zasadniczy', variable=v4, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v5 = IntVar
            c5 = tk.Checkbutton(exercise_window, text='Molowy sekstowy', variable=v5, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v6 = IntVar
            c6 = tk.Checkbutton(exercise_window, text='Molowy kwartsekstowy', variable=v6, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v7 = IntVar
            c7 = tk.Checkbutton(exercise_window, text='Zmniejszony zasadniczy', variable=v7, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v8 = IntVar
            c8 = tk.Checkbutton(exercise_window, text='Zmniejszony sekstowy', variable=v8, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v9 = IntVar
            c9 = tk.Checkbutton(exercise_window, text='Zmniejszony kwartsekstowy', variable=v9, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))
            v10 = IntVar
            c10 = tk.Checkbutton(exercise_window, text='Zwiększony kwartsekstowy', variable=v10, onvalue=1, offvalue=0,
                                font=('Comic Sans MS', 15, 'bold'))

            intervals_label = tk.Label(exercise_window,
                                       text="Odznacz trójdźwięki, których nie chcesz słuchać",
                                       font=('Comic Sans MS', 18, 'bold italic'),
                                       )
            intervals_label.place(x=450, y=130, anchor="center")
            c1.select()
            c2.select()
            c3.select()
            c4.select()
            c5.select()
            c6.select()
            c7.select()
            c8.select()
            c9.select()
            c10.select()
            c1.place(x=350, y=160)
            c2.place(x=350, y=190)
            c3.place(x=350, y=220)
            c4.place(x=350, y=250)
            c5.place(x=350, y=280)
            c6.place(x=350, y=310)
            c7.place(x=350, y=340)
            c8.place(x=350, y=350)
            c9.place(x=350, y=380)
            c10.place(x=350, y=410)
        #trójdzwieki
        exercise_start_button = tk.Button(
            exercise_window,
            bg="red",
            fg="white",
            width=15,
            text="START!",
            font=('Comic Sans MS', 10, 'bold'),
            )
        exercise_start_button.place(x = 350, y = 600)

        exercise_window.mainloop()


def main():
    App(initial)
    initial.mainloop()


if __name__ == "__main__":
    main()
