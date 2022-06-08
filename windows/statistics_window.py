import os
import sqlite3
import tkinter as tk
# import pandas as pd
import datetime

from enum_types import Exercise
from .base_window import BaseWindow
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class StatisticsWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 550, 550, "Statistics")

        database_path = os.path.join(os.path.dirname(__file__), "../main_database")
        con = sqlite3.connect(database_path)
        cursor = con.cursor()

        fig = plt.figure()
        axis = fig.add_subplot(111)
        exercises = ["Intervals", "Dominants 7th", "Triads"]
        avgs = [100*self.average_exercise_score(x, cursor) for x in Exercise]

        axis.bar(exercises, avgs)

        chart_type = FigureCanvasTkAgg(fig, self)
        chart_type.get_tk_widget().pack()

        axis.set_title('Your average statistics')

        self.longest_streak_label = tk.Label(
            self,
            bg="green",
            fg="white",
            width=20,
            text="Your longest streak: " + str(self.longest_streak(cursor)),
            font=('Comic Sans MS', 15, 'bold italic'),
        )

        self.longest_streak_label.place(x=155, y=500)

        cursor.close()

    def longest_streak(self, cursor):
        if self.master_root.logged_user is None:
            return 0

        cursor.execute(
            "SELECT distinct done_date from Scores S "
            "INNER JOIN Types T on T.ex_type = S.ex_type "
            "WHERE username = ?",
            (self.master_root.logged_user, )
        )

        select_res = cursor.fetchall()

        date_to_compare = datetime.datetime.strptime(select_res[0][0], "%Y-%m-%d")
        date_to_compare -= datetime.timedelta(days=1)

        curr_longest_streak = 0
        max_longest_streak = 0

        for next_date in select_res:
            date_to_compare += datetime.timedelta(days=1)
            datetime_next_day = datetime.datetime.strptime(next_date[0], "%Y-%m-%d")
            if date_to_compare != datetime_next_day:
                date_to_compare = datetime_next_day
                max_longest_streak = max(max_longest_streak, curr_longest_streak)
                curr_longest_streak = 0
            curr_longest_streak += 1

        return max(max_longest_streak, curr_longest_streak)

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
        return select_res[0][1]/select_res[0][0] if select_res else 0

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
