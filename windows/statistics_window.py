import tkinter as tk
from .base_window import BaseWindow


class StatisticsWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root)

        self.title("Statistics")
        self.geometry("850x600")

