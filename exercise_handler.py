from enum_types import Instrument, Mode, Exercise
import random
import os
import pygame
from pydub.playback import play
from pydub import AudioSegment

# TODO KOLEJNOSC
dom_7_options = ['zas', 'kw_sek', 'ter_kw', 'sek']
triad_options = ['dur_z', 'dur_6', 'dur_64', 'mol_z', 'mol_6', 'mol_64',
                 'zmn_z', 'zmn_6', 'zmn_64', 'zwiek']
interval_options = ['2_m', '2_w', '3_m', '3_w', '3_z_tryt' '4', '5', '6_m', '6_w', '7_m', '7_w', '8']


class ExerciseHandler:
    def __init__(self, instrument, exercise, harmonics, sounds, mode):
        self.harmonics = harmonics
        self.mode = mode
        self.instrument = instrument
        self.sounds = []
        self.playlist = []
        self.playlist_ans = []
        self.exercise = exercise
        pygame.mixer.init()
        self.instrument = instrument
        self.song = None
        self.sound_type = None
        self.path = os.path.join(os.path.dirname(__file__), "sounds/")
        for i in range(0, len(sounds), 1):
            self.sounds.append(sounds[i].get())

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
            for i in range(0, len(self.sounds), 1):
                if self.sounds[i]:
                    pass

    def check_accuracy(self, num):
        names_tab = triad_options
        if self.exercise == Exercise.INTERVALS:
            names_tab = interval_options
        elif self.exercise == Exercise.DOMINANT_7TH:
            names_tab = dom_7_options

        res = "WRONG!"
        
        if names_tab.index(self.sound_type) == num:
            res = "CORRECT!"

        print(names_tab.index(self.sound_type), num)
        print(res)

    def next_sound(self):
        self.sound_type = random.choice(os.listdir(self.path))
        self.song = self.path + self.sound_type + '/' + random.choice(os.listdir(self.path + self.sound_type))
        print(self.song)
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=0)

    def repeat_sound(self):
        if self.song is None:
            return
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=0)
