import os
import sqlite3
import tkinter as tk
from .base_window import BaseWindow
from .create_account_window import CreateAccountWindow
# import csv


class LoginWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 500, 380, "Log in")

        database_path = os.path.join(os.path.dirname(__file__), "../main_database")
        self.con = sqlite3.connect(database_path)
        self.cursor = self.con.cursor()

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
            font=('Comic Sans MS', 10, 'bold'),
            command=lambda: self.log_in(self.username_input.get(), self.password_input.get())
        )

        self.new_account_button = tk.Button(
            self,
            bg="pink",
            fg="black",
            width=20,
            text="Create a new account!",
            font=('Comic Sans MS', 10, 'bold'),
            command=self.add_user
        )

        self.login_label = tk.Label(
            self,
            font=('Comic Sans MS', 15),
        )

        self.username_label.place(x=130, y=50)
        self.username_input.place(x=230, y=55)

        self.password_label.place(x=130, y=100)
        self.password_input.place(x=230, y=105)

        self.login_button.place(x=200, y=150)
        self.new_account_button.place(x=175, y=270)

    def add_user(self):
        if not self.create_account_opened:
            window = CreateAccountWindow(self)
            window.mainloop()

    def log_in(self, username, password):
        self.login_label.place_forget()

        self.password_input.delete(0, len(password))
        self.username_input.delete(0, len(username))

        self.cursor.execute("SELECT password FROM Users WHERE username=(?)", (username, ))
        next_id = self.cursor.fetchall()

        if not next_id:
            self.login_label['text'] = "Invalid username!"
            self.login_label.place(x=180, y=210)
        elif not next_id[0][0] == password:
            self.login_label['text'] = "Invalid password!"
            self.login_label.place(x=180, y=210)
        else:
            self.master_root.log_in_button['text'] = "Log out"
            self.master_root.log_in_button['command'] = self.master_root.log_out
            self.master_root.logged_label['text'] = "Hi, " + username + "!"
            self.master_root.logged_user = username
            self.destroy()

    def set_opened(self, val):
        self.master_root.login_opened = val

    def destroy(self):
        self.con.commit()
        self.cursor.close()
        super().destroy()

    # OLD VERSION
    # def log_in(self, username, password):
    #     self.login_label.place_forget()
    #
    #     self.password_input.delete(0, len(password))
    #     self.username_input.delete(0, len(username))
    #
    #     user_exists = False
    #     correct_password = False
    #     with open('users_passwords.csv', 'r') as csvfile:
    #         csv_reader = csv.reader(csvfile, delimiter=',')
    #         for row in csv_reader:
    #             if row[0] == username:
    #                 user_exists = True
    #                 if password == row[1]:
    #                     correct_password = True
    #                 break
    #
    #     if not user_exists:
    #         self.login_label['text'] = "Invalid username!"
    #         self.login_label.place(x=180, y=210)
    #     elif not correct_password:
    #         self.login_label['text'] = "Invalid password!"
    #         self.login_label.place(x=180, y=210)
    #     else:
    #         # self.login_label['text'] = "Logged in successfully!"
    #         # self.login_label.place(x=160, y=210)
    #         self.master_root.log_in_button['text'] = "Log out"
    #         self.master_root.log_in_button['command'] = self.master_root.log_out
    #         self.master_root.logged_label['text'] = "Hi, " + username + "!"
    #         self.master_root.logged_user = username
    #         self.destroy()
