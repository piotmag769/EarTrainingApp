import tkinter as tk
from .base_window import BaseWindow


class ImprovementWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 850, 600, "Areas to improve")

