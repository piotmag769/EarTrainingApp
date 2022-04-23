import tkinter as tk


class BaseWindow(tk.Toplevel):
    def __init__(self, master_root):
        super().__init__(master_root)
        self.wm_resizable(False, False)

        self.master_root = master_root

        self.set_opened(True)

    def destroy(self):
        self.set_opened(False)
        super().destroy()

    def set_opened(self, val):
        if type(self).__name__ == "ExerciseWindow":
            self.master_root.exercise_opened = val
        elif type(self).__name__ == "ImprovementWindow":
            self.master_root.improvement_opened = val
        elif type(self).__name__ == "InfoWindow":
            self.master_root.info_opened = val
        if type(self).__name__ == "LoginWindow":
            self.master_root.login_opened = val
        if type(self).__name__ == "StatisticsWindow":
            self.master_root.statistics_opened = val
