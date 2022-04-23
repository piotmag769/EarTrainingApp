import tkinter as tk


class InfoWindow(tk.Toplevel):
    def __init__(self, master_root, already_opened):
        if already_opened:
            super().destroy()
            return

        super().__init__(master_root)
        self.wm_resizable(False, False)
        self.title("Information about program")
        self.geometry("850x600")

        self.master_root = master_root

        self.master_root.info_opened = True

    def destroy(self):
        self.master_root.info_opened = False
        super().destroy()
