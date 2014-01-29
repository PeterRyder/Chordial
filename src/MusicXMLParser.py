# Music XML Parser

# Authors: Peter Ryder, Jake Lowey, Mark Westerhoff

#### API Imports #####

from music21 import *
from numpy import *
from scipy import *

######################

import xml.etree.ElementTree as ET

print ""

class MusicXMLParser():
    song_title = ""
    work_title = ""
    work_number = ""
    song_author = ""
    encoding_date = ""
    software = []
    part_group = {}
    file_string = ""  
    sheet = ""

    def __init__(self):
        self.song_title = ""
        self.song_author = ""
        selfencoding_date = ""
        self.software = []
        self.part_group = {}
        self.file_string = "" 
        self.work_title = ""
        self.work_number = ""
        self.sheet = ""
          
    def getBasicInfo(self, input_file_string):
        global file_string
        global song_author
        global encoding_date
        global song_title
        global work_title
        global work_number
        
        self.file_string = input_file_string
        tree = ET.parse(self.file_string)
        root = tree.getroot()    
        for movement_title in root.findall('movement-title'):
            self.song_title = movement_title.text
        for work in root.findall('work'):
            for work_title in work.findall('work-title'):
                self.work_title = work_title.text
            for work_number in work.findall('work-number'):
                self.work_number = work_number.text
            
        for identification in root.findall('identification'):
            for child1 in identification:
                if child1.tag == 'creator':
                    self.song_author = child1.text
                for child2 in child1:
                    if child2.tag == 'encoding-date':
                        self.encoding_date = child2.text
                    if child2.tag == 'software':
                        self.software.append(child2.text)
    
        count = 1
        for part_list in root.findall('part-list'):
            for i in part_list:
                if i.tag == 'score-part':
                    for j in i:
                        for m in j:
                            if m.tag == 'instrument-name':
                                self.part_group[count] = m.text
                                count += 1
                                
    def getNotes(self):
        global sheet
        self.sheet = converter.parse(self.file_string)
        
    

    