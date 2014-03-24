# Music Analysis

# Authors: Peter Ryder, Jake Lowey, Mark Westerhoff

#### API Imports #####

from music21 import *
import math

######################

# (rediculous)reciculous dictionary to store all the chord combinations


######################



# run through the data structure for all of P1 in Treble cleff
#    find all the chords and notes

# run through the data structure for all of P1 in Bass cleff (if applicable
#    find all the chords and notes

# continue the above process for P2, P3, P4...



class MusicAnalysis():
    musicParsed = None
    keySignature = None
    clef = None
    
    def __init__(self, input_data_structure):
        self.musicParsed = input_data_structure
	
    def getKeySignature(self, measureNumber):
	global musicParsed
	global keySignature
	
	for voice in self.musicParsed.sheet.getElementsByClass('Part'):
	    for measure in voice.getElementsByClass('Measure'):	
		if measure.number == measureNumber:
		    for keySignature1 in measure.getElementsByClass('KeySignature'):
			amountOfSharps = keySignature1.sharps
	    
			# gets the mode of the piece
			mode = keySignature1.mode
			majors = {0:"C", 1:"G", 2:"D", 3:"A", 4:"E", 5:"B",6:"F#", 7:"C#", 
			          -1:"F", -2:"Bb", -3:"Eb", -4:"Ab", -5:"Db", -6:"Gb", -7:"Cb"}
			minors = {0:"A", 1:"E", 2:"B", 3:"F#", 4:"C#", 5:"G#", 6:"D#", 7:"A#",
			        -1:"D", -2:"G", -3:"C", -4:"F", -5:"Bb", -6:"Eb", -7:"Ab"}
			if mode == "major":
			    keySignature = majors[amountOfSharps]
			elif mode == "minor":
			    keySignature = minors[amountOfSharps]
    
    

    def getNumeralsByChord(self, measure):
	self.getKeySignature(measure.number)
	
	clef = None
	whichClef = None

	
	for whichClef in measure.getElementsByClass('TrebleClef'):
	    #print whichClef
	    clef = whichClef	
	    
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
		    
	    #print notesNumerals
	    
	    # store the notes in music21 note class form
	    for note in currentChord:
		notes.append(note)
	    
	    for voice1 in self.musicParsed.sheet.getElementsByClass('Part'):
		for measure1 in voice1.getElementsByClass('Measure'):
		    if measure1.number == measure.number:
			for note1 in measure1.getElementsByClass('Note'):
			    if note1.beat == chord.beat:
				if note1.measureNumber == chord.measureNumber:
				    notes.append(note1)
	    print notes	
	   # chord1 = chord.Chord(notes)
	   # getNumeral(chord1, KeySignature)


	
    #def getNumeral(self, chord1, keySign):
	
	
    #def getDiff(self, note1, note2):	    

	
    def getNumeralsByNote(self, measure):
	self.getKeySignature(measure.number)
	for whichClef in measure.getElementsByClass('TrebleClef'):
	    #print whichClef
	    clef = whichClef
	
	for note in measure.getElementsByClass('Note'):
	    notes = []
	    #print note
	    #notes.append(note)
	    
	    for voice1 in self.musicParsed.sheet.getElementsByClass('Part'):
		for measure1 in voice1.getElementsByClass('Measure'):
		    if measure1.number == measure.number:
			for note1 in measure1.getElementsByClass('Note'):
			    if note1.beat == note.beat:
				if note1.measureNumber == note.measureNumber:
				    if note not in notes:
					notes.append(note1)
	
	    if len(notes) > 1:
		print notes
	    
	
			    
    def analyzeNotes(self):
	global musicParsed
	
	for voice in self.musicParsed.sheet.getElementsByClass('Part'):
	    for measure in voice.getElementsByClass('Measure'):
		self.getNumeralsByChord(measure)
		self.getNumeralsByNote(measure)
