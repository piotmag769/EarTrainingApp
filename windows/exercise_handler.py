from enum_types import Instrument, Mode, Exercise
import random
import os
import pygame
import sqlite3
from datetime import datetime


class ExerciseHandler:
    def __init__(self, master_root, instrument, exercise, harmonics, what_to_play, mode):
        pygame.mixer.init()

        database_path = os.path.join(os.path.dirname(__file__), "../main_database")
        self.con = sqlite3.connect(database_path)
        self.cursor = self.con.cursor()
        self.logged_user = master_root.master_root.master_root.logged_user
        self.instrument = instrument
        self.exercise = exercise
        self.master_root = master_root
        self.harmonics = harmonics
        self.mode = mode
        self.instrument = instrument

        # triads
        # just have to maintain it in order of the buttons
        self.full_playlist = ['dur_z', 'dur_6', 'dur_64', 'mol_z', 'mol_6', 'mol_64', 'zmn_z', 'zmn_6', 'zmn_64', 'zwiek']

        if self.exercise == Exercise.INTERVALS:
            self.full_playlist = ['2_m', '2_w', '3_m', '3_w', '4', '4_5_tryt', '5', '6_m', '6_w', '7_m', '7_w', '8']
        elif self.exercise == Exercise.DOMINANT_7TH:
            self.full_playlist = ['zas', '1_kw_sek', '2_ter_kw', '3_sek']

        # we could use self.current_playlist.index() but it would be slower
        self.mapping = dict(zip([x for x in range(len(self.full_playlist))], self.full_playlist))
        self.playlist = []

        for i, sound in enumerate(what_to_play):
            if sound.get():  # if type of sound is chosen by user
                self.playlist.append(self.full_playlist[i])

        self.sound_type = None
        self.sound = None

        self.path = os.path.join(os.path.dirname(__file__), "../sounds/")

        if self.mode == mode.EASY:
            self.path += "easy/"
        elif self.mode == mode.MEDIUM:
            self.path += "medium/"
        else:
            self.path += "hard/"

        if self.instrument == Instrument.GUITAR:
            self.path += "guitar/"
        elif self.instrument == Instrument.PIANO:
            self.path += "piano/"
        else:
            self.path += "trumpet/"

        if self.exercise == Exercise.INTERVALS:
            self.path += "int/"
            if self.harmonics == 'melodycznie - w górę':
                self.path += "up/"
            elif self.harmonics == 'melodycznie - w dół':
                self.path += "down/"
            else:
                self.path += "harm/"
        elif self.exercise == Exercise.DOMINANT_7TH:
            self.path += "dom_7/"
            if self.harmonics == 'melodycznie - w górę':
                self.path += "up/"
            elif self.harmonics == 'melodycznie - w dół':
                self.path += "down/"
            elif self.harmonics == 'harmonicznie':
                self.path += "harm/"
            elif self.harmonics == 'melodycznie w górę + harmonicznie':
                self.path += "up_h/"
            else:
                self.path += "down_h/"
        else:
            self.path += "triads/"
            if self.harmonics == 'melodycznie - w górę':
                self.path += "up/"
            elif self.harmonics == 'melodycznie - w dół':
                self.path += "down/"
            elif self.harmonics == 'harmonicznie':
                self.path += "harm/"
            elif self.harmonics == 'melodycznie w górę + harmonicznie':
                self.path += "up_h/"
            else:
                self.path += "down_h/"

    def check_accuracy_outer(self, num):
        return lambda: self.check_accuracy(num)


    def check_accuracy(self, num):
        if self.sound is not None:
            res = "WRONG!"
            self.cursor.execute("SELECT ex_id FROM Scores ORDER BY ex_id desc LIMIT 1")
            next_id = self.cursor.fetchall()
            if not (next_id):
                next_id = 0
            else:
                next_id = next_id[0][0]

            # self.current_playlist_dict[self.sound_type] == num
            if self.mapping[num] == self.sound_type:
                res = "CORRECT!"
                self.master_root.correctness_label["text"] = "DOBRZE!"
                if self.logged_user != None:
                    self.cursor.execute("INSERT INTO Scores(ex_id, is_correct, username, instrument, mode, ex_type, done_date) VALUES(?, ?, ?, ?, ?, ?, ?)", (next_id + 1, 1, self.logged_user, self.instrument.name, self.mode.name, str(self.sound_type), str(datetime.date(datetime.now()))))

            else:
                self.master_root.correctness_label["text"] = "Źle :("
                if self.logged_user != None:
                    self.cursor.execute(
                    "INSERT INTO Scores(ex_id, is_correct, username, instrument, mode, ex_type, done_date) VALUES(?, ?, ?, ?, ?, ?, ?)",
                        (next_id + 1, 0, self.logged_user, self.instrument.name, self.mode.name, str(self.sound_type),
                         str(datetime.date(datetime.now()))))

            print("You chose", self.mapping[num])
            print("It was", self.sound_type)
            print(res)

            self.sound = None

    def next_sound(self):
        # TODO: zapisywanie statystyk do pliku, prob zrobimy jakiś file handler, żeby tam raz to zapisane miał,
        #  to się będzie edytować tam gdzie trzeba i potem jakoś na końcu zapisywać do pliku, a na początku wczytywać
        #  niby można bazę danych lokalną zrobić i pliki bazodanowe załączyć, ale czy to ma sens przy tym rozmiarze aplikacji?
        #  wątpię, ale jak Ci się chce to możesz
        self.master_root.correctness_label["text"] = ""
        self.sound_type = random.choice(self.playlist)
        self.sound = self.path + self.sound_type + '/' + random.choice(os.listdir(self.path + self.sound_type))
        print(self.sound)
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play(loops=0)

    def repeat_sound(self):
        self.master_root.correctness_label["text"] = ""
        if self.sound is not None:
            pygame.mixer.music.load(self.sound)
            pygame.mixer.music.play(loops=0)

    def destroy(self):
        self.con.commit()
        self.cursor.close()

