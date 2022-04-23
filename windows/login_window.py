import tkinter as tk
from .base_window import BaseWindow
from .create_account_window import CreateAccountWindow


class LoginWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 850, 600, "Log in")

        self.create_account_opened = False

        self.username_label = tk.Label(
            self,
            text="username:",
            font=('Comic Sans MS', 15),
        )

        self.password_label = tk.Label(
            self,
            text="password:",
            font=('Comic Sans MS', 15),
        )

        self.no_account_label = tk.Label(
            self,
            text="No account?",
            font=('Comic Sans MS', 18),
        )

        self.username_input = tk.Entry(
            self,
            font=('Comic Sans MS', 10)
        )

        self.password_input = tk.Entry(
            self,
            show="*",
            font=('Comic Sans MS', 10)
        )

        self.login_button = tk.Button(
            self,
            bg="blue",
            fg="white",
            width=15,
            text="Login",
            font=('Comic Sans MS', 10, 'bold')
        )

        self.new_account_button = tk.Button(
            self,
            bg="pink",
            fg="black",
            width=20,
            text="Create a new account!",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.add_user()
        )

        self.username_label.place(x=300, y=50)
        self.username_input.place(x=400, y=55)

        self.password_label.place(x=300, y=100)
        self.password_input.place(x=400, y=105)

        self.login_button.place(x=360, y=150)
        self.no_account_label.place(x=420, y=250, anchor="center")
        self.new_account_button.place(x=340, y=300)

    def add_user(self):
        if not self.create_account_opened:
            window = CreateAccountWindow(self)
            window.mainloop()

