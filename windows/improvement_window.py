import tkinter as tk
from .base_window import BaseWindow


class ImprovementWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root)

        self.title("Areas to improve")
        self.geometry("850x600")

