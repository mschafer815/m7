# Mackenzie Schafer 
# Last Edit: 12/13/18 
# Script Generation Character Class 
# Computational Creativity Fall 2018 


import ObjectiveClass
import random

PEOPLE = ['Amanda', 'Brad', 'Chad', 'Maria', 'Spencer', 'Marcos', 'Anika', 'Maddie', 'Chandler', 'Ethan']
PERSONALITY_TYPES = ['introvert', 'extrovert']
INTERESTS = ['swimming', 'biking', 'cooking', 'singing', 'studying', 'writing', 'reading', 'gaming', 'acting']
HOMES = ['Austin', 'Brunswick', 'New York', 'Madrid', 'LA', 'Chicago', 'Frankfort', 'Paris', 'Singapore']

NUM_HOBBIES_MIN = 1 
NUM_HOBBIES_MAX = 5 

NUM_FRIENDS_INTROVERT_MIN = 1 
NUM_FRIENDS_INTROVERT_MAX = 5
NUM_FRIENDS_EXTRAVERT_MIN = 3 
NUM_FRIENDS_EXTRAVERT_MAX = 10 

NUM_LOVE_INTERESTS_MIN = 1
NUM_LOVE_INTERESTS_MAX = 3



class Character:
    '''
    This class defines characters. Each character has a name, personality type, 
    variety of interests, friends and love interests, as well as a hometown. 
    '''

    def __init__(self, name, statement):
        ''' 
        Input: 
        Output: 
        Purpose: This initializes Character with name, personality_type, interests, friends, love interst, 
        and hometown. An objective, success val (has completed objective) and # words spoken, # self references are also ititialized. '''  
        self.name = name
        self.personality_type = self.choose_personality_type() #assigns personality type randomly
        self.interests = self.create_list_of_interests() # list of random interests 
        self.friends = self.create_list_of_friends() # list of random friends 
        self.love_interest = self.choose_love_interest() # list of crush or crushes 
        self.home = self.choose_home() # assigns a hometown
        self.objective = ObjectiveClass.Objective(statement)
        self.objective_success = False 
        self.score = 0 

     
    def get_name(self): 
        '''
        Input: none
        Output: str
        Purpose: This getter function returns this object's name variable.
        '''
        return self.name

    def choose_personality_type(self): 
        '''This function Randomly choose a personality type randomly from list of types '''
        p_type = random.choice(PERSONALITY_TYPES)
        return p_type

    def get_personality_type(self): 
        '''
        Input: none
        Output: str
        Purpose: This getter function returns this object's personality type variable.
        '''
        return self.personality_type
        
    def create_list_of_interests(self): 
        ''' 
        Input: None
        Output: list of strings
        Purpose: This function creates a list of a random number of random interests for a character 
        ''' 

        hobbies = []
        num_hobbies = random.randint(NUM_HOBBIES_MIN, NUM_HOBBIES_MAX)
        for i in range(1, num_hobbies): 
            hobbie = random.choice(INTERESTS)
            #hobbies.append(hobbie)
            if hobbie not in hobbies: # if interest not in list already, add it 
                hobbies.append(hobbie)
        return hobbies

    def get_interests(self): 
        '''
        Input: none
        Output: list of str
        Purpose: This getter function returns this object's interests variable.
        '''
        return self.interests

    def create_list_of_friends(self): 
        ''' 
        Input: None
        Output: list of strings
        Purpose: This function creates a list of a random number of random friends for a character 
        depending on their personality type
        ''' 

        friends = []
        if self.personality_type == 'extrovert': 
            num_friends = random.randint(NUM_FRIENDS_EXTRAVERT_MIN, NUM_FRIENDS_EXTRAVERT_MAX)
        else: #introvert
            num_friends= random.randint(NUM_FRIENDS_INTROVERT_MIN, NUM_FRIENDS_INTROVERT_MAX)
        
        for i in range(0, num_friends): 
            friend = random.choice(PEOPLE)
            if friend not in friends: # if interest not in list already, add it 
                friends.append(friend)

        return friends

    def get_friends(self): 
        '''
        Input: none
        Output: list of str
        Purpose: This getter function returns this object's friends variable.
        '''
        return self.friends

    def choose_love_interest(self): 
        ''' 
        Input: None
        Output: string
        Purpose: This function chooses a love interest for character based on people list. 
        '''

        love_interests = []

        num_love_interest = random.randint(NUM_LOVE_INTERESTS_MIN, NUM_LOVE_INTERESTS_MAX)
       
        for i in range(0, num_love_interest): 
            crush = random.choice(PEOPLE)
            if crush not in love_interests: # if interest not in list already, add it 
                love_interests.append(crush)

        return love_interests
        
    def get_love_interest(self): 
        '''
        Input: none
        Output: list of str
        Purpose: This getter function returns this object's love interest variable.
        '''
        return self.love_interest

    def choose_home(self): 
        ''' 
        Input: None
        Output: string
        Purpose: This function chooses a love home town for character based on home list. 
        '''
        home = random.choice(HOMES)
        return home

    def get_home(self): 
        '''
        Input: none
        Output: str
        Purpose: This getter function returns this object's home variable.
        '''
        return self.home

    def set_objective(self, statement): 
        ''' 
        Input: int
        Output: int
        Purpose: This function sets the objective index for the character based on a given value. 
        '''
        self.objective = ObjectiveClass.Objective(statement) 
        return self.objective

    def get_objective(self): 
        '''
        Input: none
        Output: int
        Purpose: This getter function returns this object's objective variable.
        '''
        return self.objective

    def achieve_objective(self): 
        '''
        Input: none
        Output: bool
        Purpose: This getter function changes this object's objective success variable to True and returns
        it.
        '''
        self.objective_success = True 
        return self.objective_success

    def get_objective_success(self): 
        return self.objective_success

    def get_score(self): 
        return self.score
    
    def add_to_score(self, points): 
        self.score += points 
        return self.score

    def __str__(self): 
        ''' 
        Input: None
        Output: string
        Purpose: This function returns an informal string version of the object. 
        '''
        
        string = ("Hi my name is " + self.name + " and I am an " + self.personality_type + " from " + 
        str(self.home) + ". \nI like " + str(self.interests) + " and " + str(self.love_interest)) 
        return string

    def __repr__(self): 
        ''' 
        Input: None
        Output: string
        Purpose: This function prints a formal string version of the object. 
        '''
        
        string = ("Name: " + self.name + "\Personality Type: " + self.personality_type + "\Hometown: " + 
        str(self.home) + "\nInterests: " + str(self.interests) + "\Love Interests: " + str(self.love_interest)) 
        return string
