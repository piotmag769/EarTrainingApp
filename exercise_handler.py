from enum_types import Instrument, Mode, Exercise
import random
import os
import pygame
from pydub.playback import play
from pydub import AudioSegment

class ExerciseHandler():

    def __init__(self, instrument, exercise, harmonics, sounds):
        self.harmonics = harmonics
        self.sounds = []
        self.exercise = exercise
        pygame.mixer.init()
        self.instrument = instrument
        for i in range(0, len(sounds), 1):
            self.sounds.append(sounds[i].get())



    def check_accuracy(self):
        pass

    def next_sound(self):
        path = "C:\\Users\\dorot\\Music\\svt"
        files = os.listdir(path)
        d = random.choice(files)
        #song = AudioSegment.from_mp3("C:\\Users\\dorot\\Music\\ymmd\\" + d)
        self.song = "C:\\Users\\dorot\\Music\\svt\\" + d
        #play(song)
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=0)

    def repeat_sound(self):
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=0)

