import tkinter as tk


class BaseWindow(tk.Toplevel):
    def __init__(self, master_root, width, height, title):
        super().__init__(master_root)
        self.wm_resizable(False, False)
        self.geometry(str(width) + "x" + str(height))
        self.title(title)

        self.master_root = master_root

        self.set_opened(True)

        self.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.winfo_screenwidth() - width) / 2
        y = (self.winfo_screenheight() - height) / 2
        self.geometry("+%d+%d" % (x, y))

    def destroy(self):
        self.set_opened(False)
        super().destroy()

    def set_opened(self, val):
        if type(self).__name__ == "ChooseExerciseWindow":
            self.master_root.choose_exercise_opened = val
        elif type(self).__name__ == "ImprovementWindow":
            self.master_root.improvement_opened = val
        elif type(self).__name__ == "InfoWindow":
            self.master_root.info_opened = val
        elif type(self).__name__ == "LoginWindow":
            self.master_root.login_opened = val
        elif type(self).__name__ == "StatisticsWindow":
            self.master_root.statistics_opened = val
        elif type(self).__name__ == "CreateAccountWindow":
            self.master_root.create_account_opened = val
        elif type(self).__name__ == "ExerciseWindow":
            self.master_root.exercise_window_opened = val
