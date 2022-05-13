from enum_types import Instrument, Mode, Exercise
import random
import os
import pygame
from pydub.playback import play
from pydub import AudioSegment

dom_7_options = ['zas', 'kw_sek', 'ter_kw', 'sek']
triad_options = ['dur_z', 'dur_6', 'dur_64', 'mol_z', 'mol_6', 'mol_64',
                 'zmn_z', 'zmn_6', 'zmn_64', 'zwiek']
interval_options = ['2_m', '2_w', '3_m', '3_w', '4', 'tryt', '5', '6_m', '6_w', '7_m', '7_w', '8']


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
        path = "C:\\Users\\dorot\\Documents\\STUDIA_materialy\\SEMESTR4\\Python\\projekt\\EarTrainingApp\\sounds\\"
        for i in range(0, len(sounds), 1):
            self.sounds.append(sounds[i].get())

        if self.mode == mode.EASY:
            path += "easy\\"
        elif self.mode == mode.MEDIUM:
            path += "medium\\"
        else:
            path += "hard\\"

        if self.instrument == Instrument.GUITAR:
            path += "guitar\\"
        elif self.instrument == Instrument.PIANO:
            path += "piano\\"
        else:
            path += "trumpet\\"

        if self.exercise == Exercise.INTERVALS:
            path += "int\\"
            if self.harmonics == 'melodycznie - w górę':
                path += "up\\"
            elif self.harmonics == 'melodycznie - w dół':
                path += "down\\"
            else:
                path += "harm\\"
        elif self.exercise == Exercise.DOMINANT_7TH:
            path += "dom_7\\"
            if self.harmonics == 'melodycznie - w górę':
                path += "up\\"
            elif self.harmonics == 'melodycznie - w dół':
                path += "down\\"
            elif self.harmonics == 'harmonicznie':
                path += "harm\\"
            elif self.harmonics == 'melodycznie w górę + harmonicznie':
                path += "up_h\\"
            else:
                path += "down_h\\"
        else:
            path += "triads\\"
            if self.harmonics == 'melodycznie - w górę':
                path += "up\\"
            elif self.harmonics == 'melodycznie - w dół':
                path += "down\\"
            elif self.harmonics == 'harmonicznie':
                path += "harm\\"
            elif self.harmonics == 'melodycznie w górę + harmonicznie':
                path += "up_h\\"
            else:
                path += "down_h\\"
            for i in range(0, len(self.sounds), 1):
                if self.sounds[i]:
                    pass

    def check_accuracy(self):
        pass

    def next_sound(self):
        path = "C:\\Users\\dorot\\Music\\svt"
        files = os.listdir(path)
        d = random.choice(files)
        # song = AudioSegment.from_mp3("C:\\Users\\dorot\\Music\\ymmd\\" + d)
        self.song = "C:\\Users\\dorot\\Music\\svt\\" + d
        # play(song)
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=0)

    def repeat_sound(self):
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=0)
