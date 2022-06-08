import os
import sqlite3
import tkinter as tk
from .base_window import BaseWindow
from enum_types import Exercise


class TopScoresWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 463, 170, "Top scores")

        database_path = os.path.join(os.path.dirname(__file__), "../main_database")
        con = sqlite3.connect(database_path)
        cursor = con.cursor()

        self.list_boxes = [tk.Listbox(self, font=('Comic Sans MS', 12, 'italic'), width=15) for _ in range(3)]

        for i, exercise in enumerate(Exercise):
            top_users = self.top_exercise_users(exercise, cursor)
            for j, (user_and_score, emote) in enumerate(zip(top_users, ['\U0001F947', '\U0001F948', '\U0001F949'])):
                user, score = user_and_score
                self.list_boxes[i].insert(j + 1, emote + ' ' + user)

        for list_box, exercise in zip(self.list_boxes, Exercise):
            list_box.insert(0, exercise.name)
            list_box.pack(side=tk.LEFT)

        cursor.close()

    @staticmethod
    def top_exercise_users(exercise: Exercise, cursor):
        cursor.execute(
            "SELECT username, CAST(SUM(S.is_correct) as float)/CAST(COUNT(S.ex_type) as float) as score "
            "FROM Scores S INNER JOIN Types T on T.ex_type = S.ex_type "
            "WHERE main_category = ? "
            "GROUP BY username "
            "ORDER BY score DESC "
            "LIMIT 3",
            (exercise.name, )
        )

        return cursor.fetchall()

    def set_opened(self, val):
        self.master_root.top_scores_opened = val
