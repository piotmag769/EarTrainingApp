import os
import sqlite3
import tkinter as tk
import pandas as pd

from enum_types import Exercise
from .base_window import BaseWindow
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class StatisticsWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 550, 475, "Statistics")

        database_path = os.path.join(os.path.dirname(__file__), "../main_database")
        con = sqlite3.connect(database_path)
        cursor = con.cursor()

        fig = plt.figure()
        ax = fig.add_subplot(111)
        exercises = ["Intervals", "Dominants 7th", "Triads"]
        avgs = [100*self.average_exercise_score(x, cursor) for x in Exercise]

        ax.bar(exercises, avgs)

        chart_type = FigureCanvasTkAgg(fig, self)
        chart_type.get_tk_widget().pack()

        ax.set_title('Your average statistics')

        cursor.close()

    def average_exercise_score(self, exercise: Exercise, cursor):
        main_category = exercise.name

        cursor.execute(
            "SELECT COUNT(S.ex_type), SUM(S.is_correct) FROM Scores S "
            "JOIN Types T on T.ex_type=S.ex_type "
            "WHERE s.username=? AND t.main_category=? "
            "GROUP BY username",
            (self.master_root.logged_user, main_category)
        )

        select_res = cursor.fetchall()
        res = select_res[0][1]/select_res[0][0] if select_res else 0

        return res

    def set_opened(self, val):
        self.master_root.statistics_opened = val

    # OLD VERSION
    # def average_exercise_score(self, exercise: Exercise):
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
    #     res = 0.0
    #     num = 0
    #     temp = [None, None]
    #
    #     if not var.empty:
    #         for index, column in enumerate(var):
    #             if index == 0:
    #                 continue
    #             if index % 2 == 1:
    #                 temp[0] = int(var[column].iloc[0])
    #             else:
    #                 temp[1] = int(var[column].iloc[0])
    #                 num += 1
    #                 res += temp[0] / temp[1]
    #         res = res / num
    #
    #     return res
