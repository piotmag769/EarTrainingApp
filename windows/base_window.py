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

    # virtual method
    def set_opened(self, val):
        pass
