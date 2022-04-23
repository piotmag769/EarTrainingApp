import tkinter as tk
import csv
from .base_window import BaseWindow


class CreateAccountWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 420, 250, "Create new account")

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

        self.username_input = tk.Entry(
            self,
            font=('Comic Sans MS', 10)
        )

        self.password_input = tk.Entry(
            self,
            show="*",
            font=('Comic Sans MS', 10)
        )

        self.create_account_button = tk.Button(
            self,
            bg="blue",
            fg="white",
            width=15,
            text="Create account",
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.create_new_account(self.username_input.get(), self.password_input.get())
        )

        self.warning_label = tk.Label(
            self,
            font=('Comic Sans MS', 15)
        )

        self.username_label.place(x=90, y=50)
        self.username_input.place(x=190, y=55)

        self.password_label.place(x=90, y=100)
        self.password_input.place(x=190, y=105)

        self.create_account_button.place(x=160, y=157)

    def create_new_account(self, username, password):
        self.warning_label.place_forget()

        if len(username) == 0:
            self.warning_label['text'] = "No username provided!"
            self.warning_label.place(x=100, y=200)
            return

        user_exists = False
        with open('users_passwords.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                if row[0] == username:
                    user_exists = True
                    break

        if user_exists:
            self.warning_label['text'] = "Username already exists!"
            self.warning_label.place(x=90, y=200)
            return

        if len(password) < 5:
            self.warning_label['text'] = "Your password is too short!"
            self.warning_label.place(x=90, y=200)
            return

        with open('users_passwords.csv', 'a', newline='\n') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerow([username, password])
            self.warning_label['text'] = "Account created successfully!"
            self.warning_label.place(x=85, y=200)
