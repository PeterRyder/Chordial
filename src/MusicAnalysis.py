# Music Analysis

# Authors: Peter Ryder, Jake Lowey, Mark Westerhoff

#### API Imports #####

from music21 import *
import math

######################

# rediculous dictionary to store all the chord combinations

chordDictionary = {"Cmaj": ["C", "E", "G"], "C#maj": ["C#", "F", "G#"], "Dmaj": ["D", "F#", "A"], "D#maj": ["D#", "G", "A#"], "Emaj": ["E", "G#", "B"], "Fmaj": ["F", "A", "C"], "F#maj": ["F#", "A#", "C#"], "Gmaj": ["G", "B", "D"], "G#maj": ["G#", "C", "D#"], "Amaj": ["A", "C#", "E"], "A#maj": ["A#", "D", "F"], "Bmaj": ["B", "D#", "F#"], "Cm": ["C", "D#", "G"], "C#m": ["C#", "E", "G#"], "Dm": ["D", "F", "A"], "D#m": ["D#", "F#", "A#"], "Em": ["E", "G", "B"], "Fm": ["F", "G#", "C"], "F#m": ["F#", "A", "C#"], "Gm": ["G", "A#", "D"], "G#m": ["G#", "B", "D#"], "Am": ["A", "C", "E"], "A#m": ["A#", "C#", "F"], "Bm": ["B", "D", "F#"], "C7": ["C", "E", "G", "A#"], "C#7": ["C#", "F", "G#", "B"], "D7": ["D", "F#", "A", "C"], "D#7": ["D#", "G", "A#", "C#"], "E7": ["E", "G#", "B", "D"], "F7": ["F", "A", "C", "D#"], "F#7": ["F#", "A#", "C#", "E"], "G7": ["G", "B", "D", "F"], "G#7": ["G#", "C", "D#", "F#"], "A7": ["A", "C#", "E", "G"], "A#7": ["A#", "D", "F", "G#"], "B7": ["B", "D#", "F#", "A"], "Cmin7": ["C", "D#", "G", "A#"], "C#min7": ["C#", "E", "G#", "B"], "Dmin7": ["D", "F", "A", "C"], "D#min7": ["D#", "F#", "A#", "C#"], "Emin7": ["E", "G", "B", "D"], "Fmin7": ["F", "G#", "C", "D#"], "F#min7": ["F#", "A", "C#", "E"], "Gmin7": ["G", "A#", "D", "F"], "G#min7": ["G#", "B", "D#", "F#"], "Amin7": ["A", "C", "E", "G"], "A#min7": ["A#", "C#", "F", "G#"], "Bmin7": ["B", "D", "F#", "A"], "Cmaj7": ["C", "E", "G", "B"], "C#maj7": ["C#", "F", "G#", "C"], "Dmaj7": ["D", "F#", "A", "C#"], "D#maj7": ["D#", "G", "A#", "D"], "Emaj7": ["E", "G#", "B", "D#"], "Fmaj7": ["F", "A", "C", "E"], "F#maj7": ["F#", "A#", "C#", "F"], "Gmaj7": ["G", "B", "D", "F#"], "G#maj7": ["G#", "C", "D#", "G"], "Amaj7": ["A", "C#", "E", "G#"], "A#maj7": ["A#", "D", "F", "A"], "Bmaj7": ["B", "D#", "F#", "A#"], "Csus4": ["C", "F", "G"], "C#sus4": ["C#", "F#", "G#"], "Dsus4": ["D", "G", "A"], "D#sus4": ["D#", "G#", "A#"], "Esus4": ["E", "A", "B"], "Fsus4": ["F", "A#", "C"], "F#sus4": ["F#", "B", "C#"], "Gsus4": ["G", "C", "D"], "G#sus4": ["G#", "C#", "D#"], "Asus4": ["A", "D", "E"], "A#sus4": ["A#", "D#", "F"], "Bsus4": ["B", "E", "F#"], "C7sus4": ["C", "F", "G", "A#"], "C#7sus4": ["C#", "F#", "G#", "B"], "D7sus4": ["D", "G", "A", "C"], "D#7sus4": ["D#", "G#", "A#", "C#"], "E7sus4": ["E", "A", "B", "D"], "F7sus4": ["F", "A#", "C", "D#"], "F#7sus4": ["F#", "B", "C#", "E"], "G7sus4": ["G", "C", "D", "F"], "G#7sus4": ["G#", "C#", "D#", "F#"], "A7sus4": ["A", "D", "E", "G"], "A#7sus4": ["A#", "D#", "F", "G#"], "B7sus4": ["B", "E", "F#", "A"], "C6": ["C", "E", "G", "A"], "C#6": ["C#", "F", "G#", "A#"], "D6": ["D", "F#", "A", "B"], "D#6": ["D#", "G", "A#", "C"], "E6": ["E", "G#", "B", "C#"], "F6": ["F", "A", "C", "D"], "F#6": ["F#", "A#", "C#", "D#"], "G6": ["G", "B", "D", "E"], "G#6": ["G#", "C", "D#", "F"], "A6": ["A", "C#", "E", "F#"], "A#6": ["A#", "D", "F", "G"], "B6": ["B", "D#", "F#", "G#"], "Cmin6": ["C", "D#", "G", "A"], "C#min6": ["C#", "E", "G#", "A#"], "Dmin6": ["D", "F", "A", "B"], "D#min6": ["D#", "F#", "A#", "C"], "Emin6": ["E", "G", "B", "C#"], "Fmin6": ["F", "G#", "C", "D"], "F#min6": ["F#", "A", "C#", "D#"], "Gmin6": ["G", "A#", "D", "E"], "G#min6": ["G#", "B", "D#", "F"], "Amin6": ["A", "C", "E", "F#"], "A#min6": ["A#", "C#", "F", "G"], "Bmin6": ["B", "D", "F#", "G#"], "Cdim": ["C", "D#", "F#"], "C#dim": ["C#", "E", "G"], "Ddim": ["D", "F", "G#"], "D#dim": ["D#", "F#", "A"], "Edim": ["E", "G", "A#"], "Fdim": ["F", "G#", "B"], "F#dim": ["F#", "A", "C"], "Gdim": ["G", "A#", "C#"], "G#dim": ["G#", "B", "D"], "Adim": ["A", "C", "D#"], "A#dim": ["A#", "C#", "E"], "Bdim": ["B", "D", "F"], "Caug": ["C", "E", "G#"], "C#aug": ["C#", "F", "A"], "Daug": ["D", "F#", "A#"], "D#aug": ["D#", "G", "B"], "Eaug": ["E", "G#", "C"], "Faug": ["F", "A", "C#"], "F#aug": ["F#", "A#", "D"], "Gaug": ["G", "B", "D#"], "G#aug": ["G#", "C", "E"], "Aaug": ["A", "C#", "F"], "A#aug": ["A#", "D", "F#"], "Baug": ["B", "D#", "G"], "C7-5": ["C", "E", "F#", "A#"], "C#7-5": ["C#", "F", "G", "B"], "D7-5": ["D", "F#", "G#", "C"], "D#7-5": ["D#", "G", "A", "C#"], "E7-5": ["E", "G#", "A#", "D"], "F7-5": ["F", "A", "B", "D#"], "F#7-5": ["F#", "A#", "C", "E"], "G7-5": ["G", "B", "C#", "F"], "G#7-5": ["G#", "C", "D", "F#"], "A7-5": ["A", "C#", "D#", "G"], "A#7-5": ["A#", "D", "E", "G#"], "B7-5": ["B", "D#", "F", "A"], "C7+5": ["C", "E", "G#", "A#"], "C#7+5": ["C#", "F", "A", "B"], "D7+5": ["D", "F#", "A#", "C"], "D#7+5": ["D#", "G", "B", "C#"], "E7+5": ["E", "G#", "C", "D"], "F7+5": ["F", "A", "C#", "D#"], "F#7+5": ["F#", "A#", "D", "E"], "G7+5": ["G", "B", "D#", "F"], "G#7+5": ["G#", "C", "E", "F#"], "A7+5": ["A", "C#", "F", "G"], "A#7+5": ["A#", "D", "F#", "G#"], "B7+5": ["B", "D#", "G", "A"], "Cm7-5": ["C", "D#", "F#", "A#"], "C#m7-5": ["C#", "E", "G", "B"], "Dm7-5": ["D", "F", "G#", "C"], "D#m7-5": ["D#", "F#", "A", "C#"], "Em7-5": ["E", "G", "A#", "D"], "Fm7-5": ["F", "G#", "B", "D#"], "F#m7-5": ["F#", "A", "C", "E"], "Gm7-5": ["G", "A#", "C#", "F"], "G#m7-5": ["G#", "B", "D", "F#"], "Am7-5": ["A", "C", "D#", "G"], "A#m7-5": ["A#", "C#", "E", "G#"], "Bm7-5": ["B", "D", "F", "A"], "Cm/maj7": ["C", "D#", "G", "B"], "C#m/maj7": ["C#", "E", "G#", "C"], "Dm/maj7": ["D", "F", "A", "C#"], "D#m/maj7": ["D#", "F#", "A#", "D"], "Em/maj7": ["E", "G", "B", "D#"], "Fm/maj7": ["F", "G#", "C", "E"], "F#m/maj7": ["F#", "A", "C#", "F"], "Gm/maj7": ["G", "A#", "D", "F#"], "G#m/maj7": ["G#", "B", "D#", "G"], "Am/maj7": ["A", "C", "E", "G#"], "A#m/maj7": ["A#", "C#", "F", "A"], "Bm/maj7": ["B", "D", "F#", "A#"], "Cmaj7+5": ["C", "E", "G#", "B"], "C#maj7+5": ["C#", "F", "A", "C"], "Dmaj7+5": ["D", "F#", "A#", "C#"], "D#maj7+5": ["D#", "G", "B", "D"], "Emaj7+5": ["E", "G#", "C", "D#"], "Fmaj7+5": ["F", "A", "C#", "E"], "F#maj7+5": ["F#", "A#", "D", "F"], "Gmaj7+5": ["G", "B", "D#", "F#"], "G#maj7+5": ["G#", "C", "E", "G"], "Amaj7+5": ["A", "C#", "F", "G#"], "A#maj7+5": ["A#", "D", "F#", "A"], "Bmaj7+5": ["B", "D#", "G", "A#"], "Cmaj7-5": ["C", "E", "F#", "B"], "C#maj7-5": ["C#", "F", "G", "C"], "Dmaj7-5": ["D", "F#", "G#", "C#"], "D#maj7-5": ["D#", "G", "A", "D"], "Emaj7-5": ["E", "G#", "A#", "D#"], "Fmaj7-5": ["F", "A", "B", "E"], "F#maj7-5": ["F#", "A#", "C", "F"], "Gmaj7-5": ["G", "B", "C#", "F#"], "G#maj7-5": ["G#", "C", "D", "G"], "Amaj7-5": ["A", "C#", "D#", "G#"], "A#maj7-5": ["A#", "D", "E", "A"], "Bmaj7-5": ["B", "D#", "F", "A#"], "C9": ["C", "E", "G", "A#", "D"], "C#9": ["C#", "F", "G#", "B", "D#"], "D9": ["D", "F#", "A", "C", "E"], "D#9": ["D#", "G", "A#", "C#", "F"], "E9": ["E", "G#", "B", "D", "F#"], "F9": ["F", "A", "C", "D#", "G"], "F#9": ["F#", "A#", "C#", "E", "G#"], "G9": ["G", "B", "D", "F", "A"], "G#9": ["G#", "C", "D#", "F#", "A#"], "A9": ["A", "C#", "E", "G", "B"], "A#9": ["A#", "D", "F", "G#", "C"], "B9": ["B", "D#", "F#", "A", "C#"], "Cm9": ["C", "D#", "G", "A#", "D"], "C#m9": ["C#", "E", "G#", "B", "D#"], "Dm9": ["D", "F", "A", "C", "E"], "D#m9": ["D#", "F#", "A#", "C#", "F"], "Em9": ["E", "G", "B", "D", "F#"], "Fm9": ["F", "G#", "C", "D#", "G"], "F#m9": ["F#", "A", "C#", "E", "G#"], "Gm9": ["G", "A#", "D", "F", "A"], "G#m9": ["G#", "B", "D#", "F#", "A#"], "Am9": ["A", "C", "E", "G", "B"], "A#m9": ["A#", "C#", "F", "G#", "C"], "Bm9": ["B", "D", "F#", "A", "C#"], "Cmaj9": ["C", "E", "G", "B", "D"], "C#maj9": ["C#", "F", "G#", "C", "D#"], "Dmaj9": ["D", "F#", "A", "C#", "E"], "D#maj9": ["D#", "G", "A#", "D", "F"], "Emaj9": ["E", "G#", "B", "D#", "F#"], "Fmaj9": ["F", "A", "C", "E", "G"], "F#maj9": ["F#", "A#", "C#", "F", "G#"], "Gmaj9": ["G", "B", "D", "F#", "A"], "G#maj9": ["G#", "C", "D#", "G", "A#"], "Amaj9": ["A", "C#", "E", "G#", "B"], "A#maj9": ["A#", "D", "F", "A", "C"], "Bmaj9": ["B", "D#", "F#", "A#", "C#"], "C7+9": ["C", "E", "G", "A#", "D#"], "C#7+9": ["C#", "F", "G#", "B", "E"], "D7+9": ["D", "F#", "A", "C", "F"], "D#7+9": ["D#", "G", "A#", "C#", "F#"], "E7+9": ["E", "G#", "B", "D", "G"], "F7+9": ["F", "A", "C", "D#", "G#"], "F#7+9": ["F#", "A#", "C#", "E", "A"], "G7+9": ["G", "B", "D", "F", "A#"], "G#7+9": ["G#", "C", "D#", "F#", "B"], "A7+9": ["A", "C#", "E", "G", "C"], "A#7+9": ["A#", "D", "F", "G#", "C#"], "B7+9": ["B", "D#", "F#", "A", "D"], "C7-9": ["C", "E", "G", "A#", "C#"], "C#7-9": ["C#", "F", "G#", "B", "D"], "D7-9": ["D", "F#", "A", "C", "D#"], "D#7-9": ["D#", "G", "A#", "C#", "E"], "E7-9": ["E", "G#", "B", "D", "F"], "F7-9": ["F", "A", "C", "D#", "F#"], "F#7-9": ["F#", "A#", "C#", "E", "G"], "G7-9": ["G", "B", "D", "F", "G#"], "G#7-9": ["G#", "C", "D#", "F#", "A"], "A7-9": ["A", "C#", "E", "G", "A#"], "A#7-9": ["A#", "D", "F", "G#", "B"], "B7-9": ["B", "D#", "F#", "A", "C"], "C7+9-5": ["C", "E", "F#", "A#", "D#"], "C#7+9-5": ["C#", "F", "G", "B", "E"], "D7+9-5": ["D", "F#", "G#", "C", "F"], "D#7+9-5": ["D#", "G", "A", "C#", "F#"], "E7+9-5": ["E", "G#", "A#", "D", "G"], "F7+9-5": ["F", "A", "B", "D#", "G#"], "F#7+9-5": ["F#", "A#", "C", "E", "A"], "G7+9-5": ["G", "B", "C#", "F", "A#"], "G#7+9-5": ["G#", "C", "D", "F#", "B"], "A7+9-5": ["A", "C#", "D#", "G", "C"], "A#7+9-5": ["A#", "D", "E", "G#", "C#"], "B7+9-5": ["B", "D#", "F", "A", "D"], "C6/9": ["C", "E", "G", "A", "D"], "C#6/9": ["C#", "F", "G#", "A#", "D#"], "D6/9": ["D", "F#", "A", "B", "E"], "D#6/9": ["D#", "G", "A#", "C", "F"], "E6/9": ["E", "G#", "B", "C#", "F#"], "F6/9": ["F", "A", "C", "D", "G"], "F#6/9": ["F#", "A#", "C#", "D#", "G#"], "G6/9": ["G", "B", "D", "E", "A"], "G#6/9": ["G#", "C", "D#", "F", "A#"], "A6/9": ["A", "C#", "E", "F#", "B"], "A#6/9": ["A#", "D", "F", "G", "C"], "B6/9": ["B", "D#", "F#", "G#", "C#"], "C9+5": ["C", "E", "G#", "A#", "D"], "C#9+5": ["C#", "F", "A", "B", "D#"], "D9+5": ["D", "F#", "A#", "C", "E"], "D#9+5": ["D#", "G", "B", "C#", "F"], "E9+5": ["E", "G#", "C", "D", "F#"], "F9+5": ["F", "A", "C#", "D#", "G"], "F#9+5": ["F#", "A#", "D", "E", "G#"], "G9+5": ["G", "B", "D#", "F", "A"], "G#9+5": ["G#", "C", "E", "F#", "A#"], "A9+5": ["A", "C#", "F", "G", "B"], "A#9+5": ["A#", "D", "F#", "G#", "C"], "B9+5": ["B", "D#", "G", "A", "C#"], "C9-5": ["C", "E", "F#", "A#", "D"], "C#9-5": ["C#", "F", "G", "B", "D#"], "D9-5": ["D", "F#", "G#", "C", "E"], "D#9-5": ["D#", "G", "A", "C#", "F"], "E9-5": ["E", "G#", "A#", "D", "F#"], "F9-5": ["F", "A", "B", "D#", "G"], "F#9-5": ["F#", "A#", "C", "E", "G#"], "G9-5": ["G", "B", "C#", "F", "A"], "G#9-5": ["G#", "C", "D", "F#", "A#"], "A9-5": ["A", "C#", "D#", "G", "B"], "A#9-5": ["A#", "D", "E", "G#", "C"], "B9-5": ["B", "D#", "F", "A", "C#"], "Cm9-5": ["C", "D#", "F#", "A#", "D"], "C#m9-5": ["C#", "E", "G", "B", "D#"], "Dm9-5": ["D", "F", "G#", "C", "E"], "D#m9-5": ["D#", "F#", "A", "C#", "F"], "Em9-5": ["E", "G", "A#", "D", "F#"], "Fm9-5": ["F", "G#", "B", "D#", "G"], "F#m9-5": ["F#", "A", "C", "E", "G#"], "Gm9-5": ["G", "A#", "C#", "F", "A"], "G#m9-5": ["G#", "B", "D", "F#", "A#"], "Am9-5": ["A", "C", "D#", "G", "B"], "A#m9-5": ["A#", "C#", "E", "G#", "C"], "Bm9-5": ["B", "D", "F", "A", "C#"], "C11": ["C", "E", "G", "A#", "D", "F"], "C#11": ["C#", "F", "G#", "B", "D#", "F#"], "D11": ["D", "F#", "A", "C", "E", "G"], "D#11": ["D#", "G", "A#", "C#", "F", "G#"], "E11": ["E", "G#", "B", "D", "F#", "A"], "F11": ["F", "A", "C", "D#", "G", "A#"], "F#11": ["F#", "A#", "C#", "E", "G#", "B"], "G11": ["G", "B", "D", "F", "A", "C"], "G#11": ["G#", "C", "D#", "F#", "A#", "C#"], "A11": ["A", "C#", "E", "G", "B", "D"], "A#11": ["A#", "D", "F", "G#", "C", "D#"], "B11": ["B", "D#", "F#", "A", "C#", "E"], "Cm11": ["C", "D#", "G", "A#", "D", "F"], "C#m11": ["C#", "E", "G#", "B", "D#", "F#"], "Dm11": ["D", "F", "A", "C", "E", "G"], "D#m11": ["D#", "F#", "A#", "C#", "F", "G#"], "Em11": ["E", "G", "B", "D", "F#", "A"], "Fm11": ["F", "G#", "C", "D#", "G", "A#"], "F#m11": ["F#", "A", "C#", "E", "G#", "B"], "Gm11": ["G", "A#", "D", "F", "A", "C"], "G#m11": ["G#", "B", "D#", "F#", "A#", "C#"], "Am11": ["A", "C", "E", "G", "B", "D"], "A#m11": ["A#", "C#", "F", "G#", "C", "D#"], "Bm11": ["B", "D", "F#", "A", "C#", "E"], "C11-9": ["C", "E", "G", "A#", "C#", "F"], "C#11-9": ["C#", "F", "G#", "B", "D", "F#"], "D11-9": ["D", "F#", "A", "C", "D#", "G"], "D#11-9": ["D#", "G", "A#", "C#", "E", "G#"], "E11-9": ["E", "G#", "B", "D", "F", "A"], "F11-9": ["F", "A", "C", "D#", "F#", "A#"], "F#11-9": ["F#", "A#", "C#", "E", "G", "B"], "G11-9": ["G", "B", "D", "F", "G#", "C"], "G#11-9": ["G#", "C", "D#", "F#", "A", "C#"], "A11-9": ["A", "C#", "E", "G", "A#", "D"], "A#11-9": ["A#", "D", "F", "G#", "B", "D#"], "B11-9": ["B", "D#", "F#", "A", "C", "E"], "C13": ["C", "E", "G", "A#", "D", "F", "A"], "C#13": ["C#", "F", "G#", "B", "D#", "F#", "A#"], "D13": ["D", "F#", "A", "C", "E", "G", "B"], "D#13": ["D#", "G", "A#", "C#", "F", "G#", "C"], "E13": ["E", "G#", "B", "D", "F#", "A", "C#"], "F13": ["F", "A", "C", "D#", "G", "A#", "D"], "F#13": ["F#", "A#", "C#", "E", "G#", "B", "D#"], "G13": ["G", "B", "D", "F", "A", "C", "E"], "G#13": ["G#", "C", "D#", "F#", "A#", "C#", "F"], "A13": ["A", "C#", "E", "G", "B", "D", "F#"], "A#13": ["A#", "D", "F", "G#", "C", "D#", "G"], "B13": ["B", "D#", "F#", "A", "C#", "E", "G#"], "Cm13": ["C", "D#", "G", "A#", "D", "F", "A"], "C#m13": ["C#", "E", "G#", "B", "D#", "F#", "A#"], "Dm13": ["D", "F", "A", "C", "E", "G", "B"], "D#m13": ["D#", "F#", "A#", "C#", "F", "G#", "C"], "Em13": ["E", "G", "B", "D", "F#", "A", "C#"], "Fm13": ["F", "G#", "C", "D#", "G", "A#", "D"], "F#m13": ["F#", "A", "C#", "E", "G#", "B", "D#"], "Gm13": ["G", "A#", "D", "F", "A", "C", "E"], "G#m13": ["G#", "B", "D#", "F#", "A#", "C#", "F"], "Am13": ["A", "C", "E", "G", "B", "D", "F#"], "A#m13": ["A#", "C#", "F", "G#", "C", "D#", "G"], "Bm13": ["B", "D", "F#", "A", "C#", "E", "G#"], "Cmaj13": ["C", "E", "G", "B", "D", "F", "A"], "C#maj13": ["C#", "F", "G#", "C", "D#", "F#", "A#"], "Dmaj13": ["D", "F#", "A", "C#", "E", "G", "B"], "D#maj13": ["D#", "G", "A#", "D", "F", "G#", "C"], "Emaj13": ["E", "G#", "B", "D#", "F#", "A", "C#"], "Fmaj13": ["F", "A", "C", "E", "G", "A#", "D"], "F#maj13": ["F#", "A#", "C#", "F", "G#", "B", "D#"], "Gmaj13": ["G", "B", "D", "F#", "A", "C", "E"], "G#maj13": ["G#", "C", "D#", "G", "A#", "C#", "F"], "Amaj13": ["A", "C#", "E", "G#", "B", "D", "F#"], "A#maj13": ["A#", "D", "F", "A", "C", "D#", "G"], "Bmaj13": ["B", "D#", "F#", "A#", "C#", "E", "G#"], "Cadd9": ["C", "E", "G", "D"], "C#add9": ["C#", "F", "G#", "D#"], "Dadd9": ["D", "F#", "A", "E"], "D#add9": ["D#", "G", "A#", "F"], "Eadd9": ["E", "G#", "B", "F#"], "Fadd9": ["F", "A", "C", "G"], "F#add9": ["F#", "A#", "C#", "G#"], "Gadd9": ["G", "B", "D", "A"], "G#add9": ["G#", "C", "D#", "A#"], "Aadd9": ["A", "C#", "E", "B"], "A#add9": ["A#", "D", "F", "C"], "Badd9": ["B", "D#", "F#", "C#"], "Cmadd9": ["C", "D#", "G", "D"], "C#madd9": ["C#", "E", "G#", "D#"], "Dmadd9": ["D", "F", "A", "E"], "D#madd9": ["D#", "F#", "A#", "F"], "Emadd9": ["E", "G", "B", "F#"], "Fmadd9": ["F", "G#", "C", "G"], "F#madd9": ["F#", "A", "C#", "G#"], "Gmadd9": ["G", "A#", "D", "A"], "G#madd9": ["G#", "B", "D#", "A#"], "Amadd9": ["A", "C", "E", "B"], "A#madd9": ["A#", "C#", "F", "C"], "Bmadd9": ["B", "D", "F#", "C#"], "Csus2": ["C", "D", "G"], "C#sus2": ["C#", "D#", "G#"], "Dsus2": ["D", "E", "A"], "D#sus2": ["D#", "F", "A#"], "Esus2": ["E", "F#", "B"], "Fsus2": ["F", "G", "C"], "F#sus2": ["F#", "G#", "C#"], "Gsus2": ["G", "A", "D"], "G#sus2": ["G#", "A#", "D#"], "Asus2": ["A", "B", "E"], "A#sus2": ["A#", "C", "F"], "Bsus2": ["B", "C#", "F#"], "C5": ["C", "G"], "C#5": ["C#", "G#"], "D5": ["D", "A"], "D#5": ["D#", "A#"], "E5": ["E", "B"], "F5": ["F", "C"], "F#5": ["F#", "C#"], "G5": ["G", "D"], "G#5": ["G#", "D#"], "A5": ["A", "E"], "A#5": ["A#", "F"], "B5": ["B", "F#"]}

######################



# run through the data structure for all of P1 in Treble cleff
#    find all the chords and notes

# run through the data strucutre for all of P1 in Bass cleff (if applicable
#    find all the chords and notes

# continue the above process for P2, P3, P4...



class MusicAnalysis():
    musicParsed = None
    keySignature = None
    clef = None
    
    def __init__(self, input_data_structure):
        self.musicParsed = input_data_structure
        
    def analyzeNotes(self):
	global musicParsed
	
        for voice in self.musicParsed.sheet.getElementsByClass('Part'):
	    for measure in voice.getElementsByClass('Measure'):
		for keySignature1 in measure.getElementsByClass('KeySignature'):
		    amountOfSharps = keySignature1.sharps
		    
		    # gets the mode of the piece
		    mode = keySignature1.mode
		    
		    # if the mode is major, get the key signature
		    if (mode == "major"):
		    
			# sets key signature to key of C
			if (amountOfSharps == 0):
			    keySignature = "C"
			
			# sets key signature to any of the signatures with sharps
			elif (amountOfSharps == 1):
			    keySignature = "G"
			elif (amountOfSharps == 2):
			    keySignature = "D"
			elif (amountOfSharps == 3):
			    keySignature = "A"
			elif (amountOfSharps == 4):
			    keySignature = "E"
			elif (amountOfSharps == 5):
			    keySignature = "B"
			elif (amountOfSharps == 6):
			    keySignature = "F#"
			elif (amountOfSharps == 7):
			    keySignature = "C#"
			    
			# sets key signature to any of the signatures with flats
			elif (amountOfSharps == -1):
			    keySignature = "F"
			elif (amountOfSharps == -2):
			    keySignature = "Bb"
			elif (amountOfSharps == -3):
			    keySignature = "Eb"
			elif (amountOfSharps == -4):
			    keySignature = "Ab"
			elif (amountOfSharps == -5):
			    keySignature = "Db"
			elif (amountOfSharps == -6):
			    keySignature = "Gb"
			elif (amountOfSharps == -7):
			    keySignature = "Cb"
			    
		    # if the mode is minor, get the key signature
		    elif (mode == minor):
			
			# if there are not sharps or flats
			if (amountOfSharps == 0):
			    keySignature = "A"
			    
			# sets key signature to any of the signatures with sharps
			elif (amountOfSharps == 1):
			    keySignature = "E"
			elif (amountOfSharps == 2):
			    keySignature = "B"
			elif (amountOfSharps == 3):
			    keySignature = "F#"
			elif (amountOfSharps == 4):
			    keySignature = "C#"
			elif (amountOfSharps == 5):
			    keySignature = "G#"
			elif (amountOfSharps == 6):
			    keySignature = "D#"
			elif (amountOfSharps == 7):
			    keySignature = "A#"
			    
			# sets key signature to any of the signatures with flats
			elif (amountOfSharps == -1):
			    keySignature = "D"
			elif (amountOfSharps == -2):
			    keySignature = "G"
			elif (amountOfSharps == -3):
			    keySignature = "C"
			elif (amountOfSharps == -4):
			    keySignature = "F"
			elif (amountOfSharps == -5):
			    keySignature = "Bb"
			elif (amountOfSharps == -6):
			    keySignature = "Eb"
			elif (amountOfSharps == -7):
			    keySignature = "Ab"			
		
		for whichClef in measure.getElementsByClass('TrebleClef'):
		    #print whichClef
		    clef = whichClef
		
		previousChord = None
		currentChord = None	
		
		for chord in measure.getElementsByClass('Chord'):
		    stl = stream.Stream()
		    # add a key signature
		    stl.append(key.Key(keySignature))
		    # add the chord
		    stl.append(chord)
		    
		    currentChord = chord
		    
		    # list containing note in numeral form relative to key
		    notesNumerals = []
		    
		    # notes in the chord in music21 note class format
		    notes = []
		    
		    # store the notes in numeral form relative to the key
		    for note in currentChord.scaleDegrees:
			if note[1] == None:
			    notesNumerals.append(note)
		    
		    # store the notes in music21 note class form
		    for note in currentChord:
			notes.append(note)
		
		    #print currentChord
		    
		    for voice2 in self.musicParsed.sheet.getElementsByClass('Part'):
			for measure2 in voice2.getElementsByClass('Measure'):
			    #print measure2
			    #print measure
			    #print ''

			    for whichClef2 in measure2.getElementsByClass('BassClef'):
				print clef
				print whichClef2
				print ''
				if clef != whichClef2:
				    print whichClef
				    print measure2
				    print voice2
				    
				    for note in measure2.getElementsByClass('Note'):
					print note
					print ''
					stl = stream.Stream()
				
					stl.append(key.Key(keySignature))
				
					stl.append(note)
				
					currentNote = note
				
					notes.append(note)
		    
		
		    print notes
		    
		# end of loop through chords in measure #
		
	    # end of loop through measures #
    
    
	# end of loop through parts #

    
    # end of analyze notes function #

    
# end of class #