'''
class Numeral():
    numeral = None
    
    def __init__(self, numeral):
        self.numeral = numeral
    
    def getNumeral(self):
        return numeral
    
    #ignore this for now
    def knownTransition(self, nextNumeral):
        return
'''     
        

class TransitionGraph():
    #for now, ugly dictionary of dictionaries to have the pointers
    transitions = None
    prevNumeral = None
    
    def __init__(self):
        self.transitions = dict()
        self.prevNumeral = None
   
   #add transition from previous roman numeral to the next one;
   #just adds it if it doesn't exist
    def addTransition(self, prevNum, nextNum):
        s = str(prevNum.scaleDegree) + str(nextNum.scaleDegree)
        if s not in self.transitions:
            self.transitions[s] = 0
        self.transitions[s] += 1
        
   #pass in class music21.roman.RomanNumeral
    def addNumeral(self, numeral1):
        if self.prevNumeral is None:
            self.prevNumeral = numeral1
        else:
            self.addTransition(self.prevNumeral, numeral1)
            self.prevNumeral = numeral1
            
    #prints all the transitions found
    def printTransitions(self):
        for i in self.transitions:
            print i[0] + "->" + i[1] + " : " + str(self.transitions[i])