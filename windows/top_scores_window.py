import tkinter as tk
from .base_window import BaseWindow


class TopScoresWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 850, 600, "Top scores")

    def set_opened(self, val):
        self.master_root.top_scores_opened = val
