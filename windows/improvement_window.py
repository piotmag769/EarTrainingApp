import collections
import os
import sqlite3
import tkinter as tk
from tkinter import ttk

from enum_types import Exercise
from .base_window import BaseWindow


class ImprovementWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 400, 140, "Areas to improve")

        database_names = [
            ['2_m', '2_w', '3_m', '3_w', '4', '4_5_tryt', '5', '6_m', '6_w', '7_m', '7_w', '8'],
            ['zas', '1_kw_sek', '2_ter_kw', '3_sek'],
            ['dur_z', 'dur_6', 'dur_64', 'mol_z', 'mol_6', 'mol_64', 'zmn_z', 'zmn_6', 'zmn_64',
             'zwiek']
        ]

        exercises_names = [
            ['Sekunda mała 2>', 'Sekundka wielka 2', 'Tercja mała 3>', 'Tercja wielka 3',
             'Kwarta czysta 4', 'Tryton 4</5>', 'Kwinta czysta 5', 'Seksta mała 6>',
             ' Seksta wielka 6',
             'Septyma mała 7', 'Septyma wielka 7<', 'Oktawa'],
            ['Zasadnicza', 'I przewrót', 'II przewrót', 'III przewrót'],
            ['Durowy zasadniczy', 'Durowy sekstowy', 'Durowy kwartsekstowy',
             'Molowy zasadniczy',
             'Molowy sekstowy', 'Molowy kwartsekstowy', 'Zmniejszony zasadniczy',
             'Zmniejszony sekstowy',
             'Zmniejszony kwartsekstowy', 'Zwiększony kwartsekstowy']
        ]

        self.mappings_for_user = [collections.defaultdict(lambda: "---", zip(db_names, ex_names)) for db_names, ex_names
                                  in zip(database_names, exercises_names)]

        self.find_weak_points()

    def find_weak_points(self):
        database_path = os.path.join(os.path.dirname(__file__), "../main_database")
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        worst_int = self.worst_exercise(Exercise.INTERVALS, cursor)
        worst_dom = self.worst_exercise(Exercise.DOMINANT_7TH, cursor)
        worst_triad = self.worst_exercise(Exercise.TRIADS, cursor)

        info_label = tk.Label(
            self,
            text="You are not logged in!" if self.master_root.logged_user is None else "Things you should work on:",
            font=('Comic Sans MS', 12, 'bold italic')
        )

        table = ttk.Treeview(self, height=3)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Comic Sans MS', 10, 'bold'))

        columns = ("Category", "Exercise", "Score")
        table['columns'] = columns

        table.column("#0", width=0, stretch=tk.NO)
        table.column("Category", anchor=tk.CENTER, width=80, stretch=tk.NO)
        table.column("Exercise", anchor=tk.CENTER, width=200, stretch=tk.NO)
        table.column("Score", anchor=tk.CENTER, width=80, stretch=tk.NO)

        for column in columns:
            table.heading(column, text=column, anchor=tk.CENTER)

        table.insert(parent='', index='end', iid=0, text='',
                     values=(
                         "Intervals", self.mappings_for_user[0][worst_int[0]],
                         str(int(worst_int[1] * 100)) + "%" if worst_int[1] != float('inf') else "---"))
        table.insert(parent='', index='end', iid=1, text='',
                     values=(
                         "Dominants", self.mappings_for_user[1][worst_dom[0]],
                         str(int(worst_dom[1] * 100)) + "%" if worst_dom[1] != float('inf') else "---"))
        table.insert(parent='', index='end', iid=2, text='',
                     values=(
                         "Triads", self.mappings_for_user[2][worst_triad[0]],
                         str(int(worst_triad[1] * 100)) + "%" if worst_triad[1] != float('inf') else "---"))

        info_label.pack()

        table.pack()

        cursor.close()

    def worst_exercise(self, exercise: Exercise, cursor):
        main_category = exercise.name

        cursor.execute(
            "SELECT T.ex_type, COUNT(S.ex_type), SUM(S.is_correct) FROM Scores S "
            "JOIN Types T on T.ex_type=S.ex_type "
            "WHERE s.username=? AND t.main_category=? "
            "GROUP BY S.ex_type",
            (self.master_root.logged_user, main_category)
        )

        select_res = cursor.fetchall()

        worst = [None, float('inf')]

        for name, all_tries, correct_tries in select_res:
            if correct_tries / all_tries < worst[1]:
                worst[0], worst[1] = name, correct_tries / all_tries

        return worst

    def set_opened(self, val):
        self.master_root.improvement_opened = val

    # OLD VERSION
    # def worst_exercise(self, exercise: Exercise):
    #     filename = ''
    #     if exercise == Exercise.INTERVALS:
    #         filename = "./statistics/intervals.csv"
    #     elif exercise == Exercise.DOMINANT_7TH:
    #         filename = "./statistics/dominants.csv"
    #     elif exercise == Exercise.TRIADS:
    #         filename = "./statistics/triads.csv"
    #
    #     df = pd.read_csv(filename)
    #     var = df.loc[df['username'] == self.master_root.logged_user]
    #
    #     worst = [None, float('inf')]
    #     temp = [None, None]
    #
    #     if not var.empty:
    #         for index, column in enumerate(var):
    #             # user label
    #             if index == 0:
    #                 continue
    #             if index % 2 == 1:
    #                 temp[0] = column
    #                 temp[1] = int(var[column].iloc[0])
    #             else:
    #                 temp[1] /= int(var[column].iloc[0])
    #                 if temp[1] < worst[1]:
    #                     worst[0], worst[1] = temp[0], temp[1]
    #
    #     return worst
