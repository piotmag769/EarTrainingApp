import tkinter as tk
from .base_window import BaseWindow


class InfoWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 850, 600, "Information about program")

