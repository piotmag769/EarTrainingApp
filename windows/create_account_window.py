import os
import sqlite3
import tkinter as tk

# import csv
from .base_window import BaseWindow


class CreateAccountWindow(BaseWindow):
    def __init__(self, master_root):
        super().__init__(master_root, 420, 250, "Create new account")

        database_path = os.path.join(os.path.dirname(__file__), "../main_database")
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()

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
        else:
            self.cursor.execute("SELECT username FROM Users WHERE username=(?)", (username,))
            next_id = self.cursor.fetchall()

            if next_id:
                self.warning_label['text'] = "Username already exists!"
                self.warning_label.place(x=90, y=200)
            elif len(password) < 5:
                self.warning_label['text'] = "Your password is too short!"
                self.warning_label.place(x=90, y=200)
                self.password_input.delete(0, len(password))
            else:
                self.cursor.execute("INSERT INTO Users(username, password) VALUES(?, ?)", (username, password))
                self.warning_label['text'] = "Account created successfully!"
                self.warning_label.place(x=85, y=200)

        self.password_input.delete(0, len(password))
        self.username_input.delete(0, len(username))

    def set_opened(self, val):
        self.master_root.create_account_opened = val

    def destroy(self):
        self.connection.commit()
        self.cursor.close()
        super().destroy()

    # OLD VERSION
    # def create_new_account(self, username, password):
    #     self.warning_label.place_forget()
    #
    #     if len(username) == 0:
    #         self.warning_label['text'] = "No username provided!"
    #         self.warning_label.place(x=100, y=200)
    #     else:
    #         user_exists = False
    #         with open('users_passwords.csv', 'r') as csvfile:
    #             csv_reader = csv.reader(csvfile, delimiter=',')
    #             for row in csv_reader:
    #                 if row[0] == username:
    #                     user_exists = True
    #                     break
    #
    #         if user_exists:
    #             self.warning_label['text'] = "Username already exists!"
    #             self.warning_label.place(x=90, y=200)
    #
    #         elif len(password) < 5:
    #             self.warning_label['text'] = "Your password is too short!"
    #             self.warning_label.place(x=90, y=200)
    #             self.password_input.delete(0, len(password))
    #         else:
    #             with open('users_passwords.csv', 'a', newline='\n') as csvfile:
    #                 csv_writer = csv.writer(csvfile, delimiter=',')
    #                 csv_writer.writerow([username, password])
    #                 self.warning_label['text'] = "Account created successfully!"
    #                 self.warning_label.place(x=85, y=200)
    #
    #     self.password_input.delete(0, len(password))
    #     self.username_input.delete(0, len(username))
