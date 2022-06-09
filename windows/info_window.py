import tkinter as tk

from .base_window import BaseWindow


class InfoWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 850, 600, "Information about the program")

        info_label1 = tk.Label(self,
                               text="Aplikacja pozwala użytkownikom na korzystanie z ćwiczeń słuchowych - rozpoznawania\ninterwałów, trójdźwięków oraz dominanty septymowej na "
                                    "różnych poziomach trudności, \nz wykorzystaniem 3 różnych instrumentów - gitary, trąbki oraz fortepianu.\n",
                               font=('Comic Sans MS', 15),
                               justify="left")
        info_label2 = tk.Label(self,
                               text="Użytkownik ma możliwość wyboru postaci, w jakiej chce słuchać dźwięków (melodycznej, \nharmonicznej, etc.)"
                                    " oraz wyboru konkretnej listy dźwięków, co daje możliwość\nindywidualizacji ćwiczeń.\n",
                               font=('Comic Sans MS', 15),
                               justify="left")

        info_label3 = tk.Label(self,
                               text="Istnieje możliwość utworzenia konta w aplikacji, aby śledzić swoje postępy i dostawać \n"
                                    "wskazówki do dalszych ćwiczeń. Możliwe jest też śledzenie regularności ćwiczeń\n"
                                    "(w postaci daily streak) oraz porównywanie wyników z innymi użytkownikami.\n",
                               font=('Comic Sans MS', 15),
                               justify="left")

        info_label4 = tk.Label(self,
                               text="Program przygotowany przez Piotra Magierę i Dorotę Meszkę w ramach zajęć z\n"
                                    "przedmiotu 'Programowanie w języku Python' na II roku informatyki AGH.\n",
                               font=('Comic Sans MS', 15),
                               justify="left")
        info_label1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5, columnspan=3)
        info_label2.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5, columnspan=3)
        info_label3.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5, columnspan=3)
        info_label4.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5, columnspan=3)

    def set_opened(self, val):
        self.master_root.info_opened = val
