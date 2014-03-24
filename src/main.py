# Main python file for MusicParser 

# Authors: Peter Ryder, Jake Lowey, Mark Westerhoff

#### API Imports ################

from music21 import *
import sys

######################

#### File Imports ####

from MusicXMLParser import *
from MusicAnalysis import *

######################

getInfo = False
parseMusic = True

if __name__ == "__main__":
    
    # future passing in from front end of file location
    fileName = sys.argv
    
    musicParsed = MusicXMLParser('../xml examples/Test2.xml')
    if getInfo:
        musicParsed.getBasicInfo()
    
        # print out interesting things about the song
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
    if parseMusic:
        musicParsed.getNotes()
        musicParsed.sheet.show("text")
        
        # analyze the music using the data structure
        musicAnalyze = MusicAnalysis(musicParsed)
        musicAnalyze.analyzeNotes()
        
        
        
        
# thread.startNewThread(functionName,(arg, args))

