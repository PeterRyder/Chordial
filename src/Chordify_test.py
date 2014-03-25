from music21 import *
from transitions import *

#uses core corpus
#BrahWiMeSample
b = corpus.parse('Test1')
#b.show('text')

bChords = b.chordify()

#adds chordify as another voice to show better
for c in bChords.flat:
    if 'Chord' not in c.classes:
        continue
    c.closedPosition(forceOctave=4, inPlace=True)

#b.measures(0,2).show()

stats = TransitionGraph()

#adds roman numerals at the bottom
for c in bChords.flat.getElementsByClass('Chord'):
    rn = roman.romanNumeralFromChord(c, key.Key('A'))
    stats.addNumeral(rn)
    c.addLyric(str(rn.figure))
#bChords.measures(0, 2).show()
bChords.show()



#prints the roman numerals, i.e. lyrics
for c in bChords.measures(0,2).flat:
    if 'Chord' not in c.classes:
        continue
    print c.lyric,
    
print "\n"
stats.printTransitions()
