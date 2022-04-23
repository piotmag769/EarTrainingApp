import tkinter as tk


class ImprovementWindow(tk.Toplevel):
    def __init__(self, master_root, already_opened):
        if already_opened:
            super().destroy()
            return

        super().__init__(master_root)
        self.wm_resizable(False, False)
        self.title("Areas to improve")
        self.geometry("850x600")

        self.master_root = master_root

        self.master_root.improvement_opened = True

    def destroy(self):
        self.master_root.improvement_opened = False
        super().destroy()
