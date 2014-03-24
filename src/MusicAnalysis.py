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

# run through the data strucutre for all of P1 in Bass cleff (if applicable
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
		
	#for note in measure.getElementsByClass('Note'):
	    #print note
			    
    def analyzeNotes(self):
	global musicParsed
	
	for voice in self.musicParsed.sheet.getElementsByClass('Part'):
	    for measure in voice.getElementsByClass('Measure'):
		self.getNumeralsByChord(measure)
		#self.getNumeralsByNote(measure)
