# main python file for MusicParser 
# authors: Peter Ryder, Jake Lowey

#### API Imports #####

from music21 import *
from numpy import *
from scipy import *

######################

#### File Imports ####

from MusicXMLParser import *
from MusicAnalysis import *
from MusicStorage import *

######################

musicParsed = MusicXMLParser()
musicParsed.getBasicInfo('BeetAnGeSample.xml')

if musicParsed.song_title != "":
    print "Song Title: " + musicParsed.song_title
if musicParsed.work_number != "":
    print "Work Number: " + musicParsed.work_number
if musicParsed.work_title != "":
    print "Work Title: " + musicParsed.work_title
if musicParsed.song_author != "":
    print "Song Author: " + musicParsed.song_author
if musicParsed.encoding_date != "":
    print "Encoding Date: " + musicParsed.encoding_date
                
print "Software used: "     
for i in musicParsed.software:
    print "  " + i
    
    
print "Instruments Used:"
i = 0
for i in musicParsed.part_group:
    print str(i) + " " + musicParsed.part_group[i]
    i+=1

print ""

# fully parse the xml
musicParsed.getNotes()
musicParsed.sheet.show('text')

# store the sheet into a data structure
## TODO ##
musicStorage = MusicStorage(musicParsed.sheet)
musicStorage.storeNotes()
## TODO ##

# temporary string to fill in for data structure
data_structure = ""

# analyze the music using the data structure
## TODO ##
musicAnalyze = MusicAnalysis(data_structure)
musicAnalyze.analyzeNotes()
## TODO ##
