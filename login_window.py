import tkinter as tk


# it inherits from Toplevel so u can use deiconify() and withdraw() on its instance
class LoginWindow(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.wm_resizable(False, False)
        self.title("Log in")
        self.geometry("850x600")
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
            font=('Comic Sans MS', 10, 'bold')
        )

        self.username_label.place(x=300, y=50)
        self.username_input.place(x=400, y=55)

        self.password_label.place(x=300, y=100)
        self.password_input.place(x=400, y=105)

        self.login_button.place(x=360, y=150)
        self.no_account_label.place(x=420, y=250, anchor="center")
        self.new_account_button.place(x=340, y=300)
