import tkinter as tk
import pandas as pd

from enum_types import Exercise
from .base_window import BaseWindow
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class StatisticsWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 850, 600, "Statistics")
        fig = plt.figure()
        ax = fig.add_subplot(111)
        exercises = ["Intervals", "Dominants 7th", "Triads"]
        avgs = []

        avgs.append(self.average_exercise_score(Exercise.INTERVALS))
        avgs.append(self.average_exercise_score(Exercise.DOMINANT_7TH))
        avgs.append(self.average_exercise_score(Exercise.TRIADS))

        ax.bar(exercises, avgs)

        chart_type = FigureCanvasTkAgg(fig, self)
        chart_type.get_tk_widget().pack()

        ax.set_title('Your average statistics')

    def average_exercise_score(self, exercise: Exercise):
        filename = ''
        if exercise == Exercise.INTERVALS:
            filename = "./statistics/intervals.csv"
        elif exercise == Exercise.DOMINANT_7TH:
            filename = "./statistics/dominants.csv"
        elif exercise == Exercise.TRIADS:
            filename = "./statistics/triads.csv"

        df = pd.read_csv(filename)
        var = df.loc[df['username'] == self.master_root.logged_user]

        res = 0.0
        num = 0
        temp = [None, None]

        if not var.empty:
            for index, column in enumerate(var):
                if index == 0:
                    continue
                if index % 2 == 1:
                    temp[0] = int(var[column].iloc[0])
                else:
                    temp[1] = int(var[column].iloc[0])
                    num += 1
                    res += temp[0] / temp[1]
            res = res / num

        return res
