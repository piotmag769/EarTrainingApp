from enum import Enum


class Instrument(Enum):
    PIANO = 0
    GUITAR = 1
    TRUMPET = 2


class Mode(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2


class Exercise(Enum):
    INTERVALS = 0
    DOMINANT_7TH = 1
    TRIADS = 2
