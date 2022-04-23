import tkinter as tk


class StatisticsWindow(tk.Toplevel):
    def __init__(self, master_root, already_opened):
        if already_opened:
            super().destroy()
            return

        super().__init__(master_root)
        self.wm_resizable(False, False)
        self.title("Statistics")
        self.geometry("850x600")

        self.master_root = master_root

        self.master_root.statistics_opened = True

    def destroy(self):
        self.master_root.statistics_opened = False
        super().destroy()
