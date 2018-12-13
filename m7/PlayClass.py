# Mackenzie Schafer 
# Last Edit: 12/13/18
# Script Generation Play Object Class 
# Computational Creativity Fall 2018 


class Play:
    '''
    This class defines Play objects. Each character has a name, character list and score. 
    '''


    def __init__(self, name):
        ''' 
        Input: none
        Output: none
        Purpose: This initializes objective with name, characterList, score and text.'''  
        self.name = name
        self.characterList = []
        self.score = 0
        self.text = [] 

    def get_score(self): 
        return self.score 

    def add_to_score(self, points): 
        self.score += points 
        return self.score

    def addCharacter(self, character): 
        self.characterList.append(character) 
        return self.characterList
    
    def getCharacterList(self): 
        return self.characterList
    
    def get_name(self): 
        return self.name

    def set_text(self, text): 
        self.text = text
        return self.text

    def get_text(self): 
        return self.text

    