# Music XML Parser

from music21 import *
import numpy
import scipy

import xml.etree.ElementTree as ET

tree = ET.parse('ActorPreludeSample.xml')
root = tree.getroot()

print ""

song_title = ''
song_author = ''
encoding_date = ''
software = []
part_group = {}

for movement_title in root.findall('movement-title'):
    song_title = movement_title.text

for identification in root.findall('identification'):
    for child1 in identification:
        if child1.tag == 'creator':
            song_author = child1.text
        for child2 in child1:
            if child2.tag == 'encoding-date':
                encoding_date = child2.text
            if child2.tag == 'software':
                software.append(child2.text)

count = 1
for part_list in root.findall('part-list'):
    for i in part_list:
        if i.tag == 'score-part':
            for j in i:
                for m in j:
                    if m.tag == 'instrument-name':
                        part_group[count] = m.text
                        count += 1

print "Song Title: " + song_title   
print "Song Author: " + song_author
print "Encoding Date: " + encoding_date
                
print "Software used: "     
for i in software:
    print "  " + i
    
print "Instruments Used:"
i = 0
for i in part_group:
    print str(i) + " " + part_group[i]
    i+=1
    
    
sheet = converter.parse('BeetAnGeSample.xml')
#sheet.show('text')
voice = sheet.getElementsByClass(stream.Part)
measures = voice.getElementsByClass(stream.Measure)
voice.show('text')

print len(measures)
print len(voice)

# converter.parse()
# chord.Chord()
    