import tkinter as tk
from tkinter import ttk
import pandas as pd
from .base_window import BaseWindow
from enum_types import Exercise


class ImprovementWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 500, 300, "Areas to improve")
        self.find_weak_points()

    def find_weak_points(self):
        worst_int = self.worst_exercise(Exercise.INTERVALS)
        worst_dom = self.worst_exercise(Exercise.DOMINANT_7TH)
        worst_triad = self.worst_exercise(Exercise.TRIADS)

        info_label = tk.Label(
            self,
            text="You are not logged in!" if self.master_root.logged_user is None else "Things you should work on:",
            font=('Comic Sans MS', 12, 'bold italic')
        )

        my_game = ttk.Treeview(self)

        columns = ("Category", "Exercise", "Score")
        my_game['columns'] = columns

        my_game.column("#0", width=0, stretch=tk.NO)
        my_game.column("Category", anchor=tk.CENTER, width=80)
        my_game.column("Exercise", anchor=tk.CENTER, width=200)
        my_game.column("Score", anchor=tk.CENTER, width=80)

        for column in columns:
            my_game.heading(column, text=column, anchor=tk.CENTER)

        my_game.insert(parent='', index='end', iid=0, text='',
                       values=("Intervals", worst_int[0], str(int(worst_int[1]*100)) + "%" if worst_int[1] != float('inf') else "None"))
        my_game.insert(parent='', index='end', iid=1, text='',
                       values=("Dominants", worst_dom[0], str(int(worst_dom[1]*100)) + "%" if worst_dom[1] != float('inf') else "None"))
        my_game.insert(parent='', index='end', iid=2, text='',
                       values=("Triads", worst_triad[0], str(int(worst_triad[1]*100)) + "%" if worst_triad[1] != float('inf') else "None" ))

        info_label.pack()

        my_game.pack()

    def worst_exercise(self, exercise: Exercise):
        filename = ''
        if exercise == Exercise.INTERVALS:
            filename = "./statistics/intervals.csv"
        elif exercise == Exercise.DOMINANT_7TH:
            filename = "./statistics/dominants.csv"
        elif exercise == Exercise.TRIADS:
            filename = "./statistics/triads.csv"

        df = pd.read_csv(filename)
        var = df.loc[df['username'] == self.master_root.logged_user]

        worst = [None, float('inf')]
        temp = [None, None]

        if not var.empty:
            for index, column in enumerate(var):
                # user label
                if index == 0:
                    continue
                if index % 2 == 1:
                    temp[0] = column
                    temp[1] = int(var[column].iloc[0])
                else:
                    temp[1] /= int(var[column].iloc[0])
                    if temp[1] < worst[1]:
                        worst[0], worst[1] = temp[0], temp[1]

        return worst
