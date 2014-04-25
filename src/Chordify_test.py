from music21 import corpus, roman, key
from transitions import *
from os import path

#uses core corpus
#BrahWiMeSample
#if .path.exists(os.path.join(os.path.expanduser("~") , "AppData\\Roaming\\Reinigen\\Logs")):
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
bChords.show('text')



#prints the roman numerals, i.e. lyrics
for c in bChords.measures(0,2).flat:
    if 'Chord' not in c.classes:
        continue
    print c.lyric,
    
print "\n"
stats.printTransitions()
