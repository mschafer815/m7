# Mackenzie Schafer 
# Last Edit: 12/13/18 
# Script Dialogue Generation Program 
# Computational Creativity Fall 2018 

# System Name: "A Little Bird" 
# 
# This function generate screenplay about Bowdoin. 
# Duet scenes with introverts and extroverts inspired by John Cariani's Almost, Maine, 
# and Francois Mairesse and Marilyn Walker's PERSONAGE: Personality 
# Generation for Dialogue paper

import CharacterClass
import ObjectiveClass
import PlayClass
import sys 
import random


NUM_PLAYS = 10
MIN_NUMBER_SCENES = 3
MAX_NUMBER_SCENES = 8 

# TODO: change these to more original options 
CHARACTER_NAMES = ["Babsie", "Sadie", "Ellie", "Ro", "Marcos", "Hannah", "Hercules", "Billy Joe Bob", "Buster"]
DAY_TIMES = ["morning", "midday", "afternoon", "night"]
EXT_PLACES = ["The Quad", "Farely", "Maine Street", "The Museum Steps", "The Polar Bear"]
INT_PLACES = ["Moulton Dark Room", "Searles 224", "Memorial Hall", "Ladd House", "HL Basement"]

OBJECTIVES_STATEMENTS = ["Hobby", "Love Interest", "Hometown", "Friends"]

INTROVERT_GREETINGS = ["Hi.", "What's up?"]
EXTROVERT_GREETINGS = ["Hey! How are you doing? I am so fantastic.", "Hi there. I am so glad to see you today."]

INTROVERT_ADJS = ["fine", "okay", "not bad", "so so"]
EXTROVERT_ADJS = ["fantastic", "incredible", "stellar", "just the bestest"]

INTROVERT_PUNCT = [".", "..."]
EXTROVERT_PUNCT = ["!"]

SUCCESSFUL_INTROVERT_GOODBYE = ["Thanks.", "See you soon.", "Okay. Till morrow."]
FAILED_INTROVERT_GOODBYE = ["Bye.", "Huh...", "Ya.", "(Pause)."]

SUCCESSFUL_EXTROVERT_GOODBYE = ["Thanks.", "See you soon.", "Okay. Till morrow."]
FAILED_EXTROVERT_GOODBYE = ["Bye.", "Huh...", "Ya.", "(Pause)."]

EXTROVERT_ACK = ["Right", "Okay", "I see", "Well", "Wild", "Fascinating"]
INTROVERT_ACK = ["Yeah", "Huh", "Hmm", "Sure"]
EXTRA_TOPICS = ["So this one time I was walking to the beach and I saw this shell and I thought it was beautiful. Do you like shells?", 
"I have never had spaghetti past midnight. I know that is super weird to say, but I mean wow! Who doesn't love a good bowl of pasta?!", 
"Have you ever scene the lights shine that bright? This is marvaleous.", "OMG calc today was so hard!", 
"I'm so glad we took that first year seminar together. Can you believe its been 3 years?!", 
"I just need you to know I am strictly a Moulton light room person.", "I think I'm going to join the BOC.", 
"It's so cold out!", "God the squirrels just get braver every year."]
DOWNWARD_HEDGES = ["sort of", "somewhat", "quite", "rather", "err", "I think that", "it seems that", "I mean"]
RANDOM_FILLER = ["I can't believe it.", "This is a lot to handle.", "What an interesting concept.", 
"I never would have thought this would happen.", "I am sure I do not know what you mean.", "(Pause).", 
"Now I've seen everything.", "What a time to be alive.", "This is not how I imagined my day going.", 
"This feels just right."]

PAUSE_POINTS = 10


def generate_setting():
    '''
    Input: none
    Output: (str, str, str)
    Purpose: This generates a time of day, location and int or ext for each scene. 
    '''
    time = random.choice(DAY_TIMES)
    abstract_place = random.choice(["EXT.", "INT."])
    place = ""
    if abstract_place == "EXT.":
        place = random.choice(EXT_PLACES)
    else:
        place = random.choice(INT_PLACES)
    return (time, abstract_place, place)

def pick_characters_and_objectives(): 
    '''
    Input: none
    Output: character, character
    Purpose: This initializes 2 character objects for a scene and give each one an objective.  
    '''

    character_A_name = random.choice(CHARACTER_NAMES)
    character_B_name = random.choice(CHARACTER_NAMES)
    # make sure A & B aren't be same character
    while character_A_name == character_B_name: 
        character_B_name = random.choice(CHARACTER_NAMES)

    # choose objectives 
    objective_a = random.choice(OBJECTIVES_STATEMENTS)
    objective_b = random.choice(OBJECTIVES_STATEMENTS)

    #initialize characters and set character objectives
    character_A = CharacterClass.Character(character_A_name, objective_a)
    character_B = CharacterClass.Character(character_B_name, objective_b)

    
    a_obj_set = set_objectives_q_and_a(character_A, character_B)
    b_obj_set = set_objectives_q_and_a(character_B, character_A)



    return character_A, character_B

def set_objectives_q_and_a(character, scene_partner): 
    '''
    Input: none
    Output: bool (True if worked) 
    Purpose: This sets the questions and answers for a character's objective object variable.  
    '''
    try: 
        if character.get_objective().get_statement() == "Hobby": 
            #question
            question = 'What is a hobby of yours?'
            answers = []
            hobby = random.choice(scene_partner.get_interests())
            answers.append(hobby)
            character.get_objective().set_question_and_answers(question, answers)
            return True 
        
        elif character.get_objective().get_statement() == "Love Interest": 
            #question
            question = 'Who do you like-like?'
            answers = []
            love_int = random.choice(scene_partner.get_love_interest())
            answers.append(love_int)
            character.get_objective().set_question_and_answers(question, answers)
            return True 
        
        elif character.get_objective().get_statement() == "Hometown": 
            #question
            question = 'Where are you from?'
            answers = []
            home = scene_partner.get_home()
            answers.append(home)
            character.get_objective().set_question_and_answers(question, answers)
            return True 
        
        elif character.get_objective().get_statement() == "Friends": 
            #question
            question = 'Who are you friends with?'
            answers = []
            friend = random.choice(scene_partner.get_friends())
            answers.append(friend)
            character.get_objective().set_question_and_answers(question, answers)
            return True 

        else: 
            print("Error: Your character doesn't have a functional objective.")
            return False
    except: 
        "ERROR: Empty list!"
        return False 
    
def generate_scene_description(character_A, character_B):
    '''
    Input: character, character
    Output: str
    Purpose: This provides a brief description of the scene-- each character and their objectives. 
    '''

    sentence1 = (character_A.get_name() + ' wants to figure out ' + character_B.get_name() + "'s "
    + str(character_A.get_objective().get_statement()) + '.')
    sentence2 = (character_B.get_name() + ' wants to figure out ' + character_A.get_name() 
    + "'s " + str(character_B.get_objective().get_statement()) + '.')

    return "Scene Description: \n" + sentence1 + "\n" + sentence2

def verbosity_cal(character, string, p_type): 
    '''
    Input: character, str
    Output: int
    Purpose: This created a verbosity score based on p_type. 
    '''
    score = 0

    if p_type == 'introvert': #reward introvert for talking less 
        if len(string) < 10: 
            score += 20
    else: 
        score += len(string)

    return score

def get_names_and_types(character_A, character_B): 
    '''
    Input: 2 characters
    Output: 4 strings
    Purpose: This function returns the 4 string names and ptypes of the 2 characters.
    '''

    #get names 
    char_a_name = character_A.get_name()
    char_b_name = character_B.get_name()

    #get personality types 
    char_a_ptype = character_A.get_personality_type() 
    char_b_ptype = character_B.get_personality_type()

    return char_a_name, char_b_name, char_a_ptype, char_b_ptype

def generate_greeting_dialogue(character_A, character_B): 
    '''
    Input: 2 characters
    Output: string
    Purpose: This function returns a string of greeting dialogue between 2 characters.
    '''

    dialogue = [] 
    
    #get names and ptypes
    char_a_name, char_b_name, char_a_ptype, char_b_ptype = get_names_and_types(character_A, character_B)

    greeting_a = generate_greeting_ptype(char_a_ptype)
    greeting_b = generate_greeting_ptype(char_b_ptype)

    dialogue.append(char_a_name + ":\n\t" + greeting_a)
    #add points to characters for verbosity according to p type
    character_A.add_to_score(verbosity_cal(character_A, greeting_a, char_a_ptype))

    if greeting_a.endswith("?"): #if a asks question, b greets and responds 
        adj = generate_adjective(char_b_ptype)
        punct = generate_punctuation(char_b_ptype)
        response = char_b_name + ":\n\t" + greeting_b + " I'm " + adj + punct
        #add verbosity points
        character_B.add_to_score(verbosity_cal(character_B, response, char_b_ptype))
        dialogue.append(response)
        

    else: 
        dialogue.append(char_b_name + ":\n\t" + greeting_b)
        character_B.add_to_score(verbosity_cal(character_B, greeting_b, char_b_ptype))
        if greeting_b.endswith("?"): # if b asks question, a responds
            adj = generate_adjective(char_a_ptype)
            punct = generate_punctuation(char_a_ptype)
            response = char_b_name + ":\n\t" + "I'm " + adj + punct
            #add verbosity points
            character_B.add_to_score(verbosity_cal(character_B, response, char_b_ptype))
            dialogue.append(response)

    return '\n\n'.join(dialogue)

def generate_greeting_ptype(p_type): 
    '''
    Input: character, str
    Output: string
    Purpose: This function returns a string of greeting based on personality type.  
    '''
    if p_type == 'introvert': 
        greeting = random.choice(INTROVERT_GREETINGS)
    else: 
        greeting = random.choice(EXTROVERT_GREETINGS)
    return greeting 

def generate_adjective(p_type): 
    '''
    Input: str
    Output: string
    Purpose: This function returns a string of an adjective based on personality type.  
    '''
    if p_type == 'introvert': 
        adj = random.choice(INTROVERT_ADJS)
    else: 
        adj = random.choice(EXTROVERT_ADJS)
    return adj 

def generate_punctuation(p_type): 
    '''
    Input: str
    Output: string
    Purpose: This function returns a string of a punctuation based on personality type.  
    '''
    if p_type == 'introvert': 
        punct = random.choice(INTROVERT_PUNCT)
    else: 
        punct = random.choice(EXTROVERT_PUNCT)
    return punct

def generate_goodbye(character_A, character_B): 
    '''
    Input: 2 characters
    Output: string
    Purpose: This function returns a string of goodbye dialogue between 2 characters.
    '''

    dialogue = [] 
    
    #get names and ptypes
    char_a_name, char_b_name, char_a_ptype, char_b_ptype = get_names_and_types(character_A, character_B)

    goodbye_a = generate_goodbye_ptype(character_A, char_a_ptype)
    goodbye_b = generate_goodbye_ptype(character_B, char_b_ptype)

    #add verbosity points
    character_A.add_to_score(verbosity_cal(character_A, goodbye_a, char_a_ptype))
    character_B.add_to_score(verbosity_cal(character_B, goodbye_b, char_b_ptype))

    dialogue.append(char_a_name + ":\n\t" + goodbye_a)
    dialogue.append(char_b_name + ":\n\t" + goodbye_b)

    dialogue.append("\n\n\n")

    return '\n\n'.join(dialogue)

def generate_goodbye_ptype(character, p_type): 
    '''
    Input: character, str
    Output: string
    Purpose: This function returns a string of goodbye based on personality type and success of 
    objective.  
    '''

    success = character.get_objective_success()

    if success: 
        if p_type == 'introvert': 
            greeting = random.choice(SUCCESSFUL_INTROVERT_GOODBYE)
        else: #extrovert
            greeting = random.choice(SUCCESSFUL_EXTROVERT_GOODBYE)

    else: 
        if p_type == 'introvert': 
            greeting = random.choice(FAILED_INTROVERT_GOODBYE)
        else: #extrovert
            greeting = random.choice(FAILED_EXTROVERT_GOODBYE)
    return greeting 

def generate_obj_attempt_dialogue(character, scene_partner):
    '''
    Input: 2 character objects
    Output: str  
    Purpose: This generates dialogue based on the character's object and scene partner
    '''
    #TODO: Generate dialogue based on personality type
    dialogue = [] 
    
    #get names 
    char_name = character.get_name()
    sp_name = scene_partner.get_name()

    #get personality types 
    char_ptype = character.get_personality_type() 
    sp_ptype = scene_partner.get_personality_type()
    
    not_finished = True

    while not_finished: # have not asked/ answered question
        num = random.randint(0, 3)
        if char_ptype == 'extrovert':
            if num > 0: # Bring up other topic and sp acknowledge
                line = bring_up_other_topic(character, scene_partner, char_name, sp_name, char_ptype, sp_ptype)
                dialogue.append(line)

            else: # Ask question 
                dialogue.append(ask_question(character, scene_partner))
                not_finished = False

        else: # introvert 
            if num > 2: # Pause and possible filler
                dialogue.append(char_name + ":\n\t" + "(Pause).")
                # add pausing points
                character.add_to_score(PAUSE_POINTS)

                ack = generate_ack_ptype(scene_partner, sp_ptype)
                punct = generate_punctuation(sp_ptype)
                line = ":\n\t" + ack + punct
                dialogue.append(char_name + line)
                #add verbosity points
                character.add_to_score(verbosity_cal(character, line, char_ptype))

                dialogue.append('\t' + generate_random_filler(character, char_ptype))
            

            else: # Ask question 
                dialogue.append(ask_question(character, scene_partner))
                not_finished = False

    return '\n\n'.join(dialogue)

def bring_up_other_topic(character, scene_partner, char_name, sp_name, char_ptype, sp_ptype): 
    '''
    Input: 2 characters and 3 strings char names and personality types)
    Output: String 
    Purpose: This is extra dialogue because extroverts tend to bring up multiple topics in conversation. 
    '''

    dialogue = [] 

    line = ":\n\t" + random.choice(EXTRA_TOPICS)
    #add verbosity points
    character.add_to_score(verbosity_cal(character, line, char_ptype))
    dialogue.append(char_name + line)

    ack = generate_ack_ptype(scene_partner, sp_ptype)
    punct = generate_punctuation(sp_ptype)
    line = ":\n\t" + ack + punct
    dialogue.append(sp_name + line)
    #add verbosity points
    scene_partner.add_to_score(verbosity_cal(scene_partner, line, sp_ptype))

    line = '\t' + generate_random_filler(scene_partner, sp_ptype)

    return '\n\n'.join(dialogue)

def ask_question(character, scene_partner): 
    '''
    Input: 2 character objects
    Output: str  
    Purpose: This generates dialogue to ask and answer a question based on the character's object 
    and scene partner and return a str of the dialogue. 
    '''
    dialogue = []

    #get names and ptypes
    char_name, sp_name, char_ptype, sp_ptype = get_names_and_types(character, scene_partner)

    # get question and answer
    question = character.get_objective().get_question()
    answer = character.get_objective().get_answer(0)
    will_answer = bool(random.randint(0,1)) # 50/50 shot of getting question answered 
    character.achieve_objective()

    dialogue.append(char_name + ":\n\t" + question)
    if will_answer: # if scene partner will answer question-- answer it. 
        dialogue.append(sp_name + ":\n\t" + answer)
    else: # 
        dialogue.append(sp_name + ":\n\t" + generate_random_filler(character, char_ptype))
    
    return '\n\n'.join(dialogue)

def generate_random_filler(character, char_ptype): 
    '''
    Input: character and string
    Output: string
    Purpose: This function returns a string of random filler at about 30% chance.  
    It also add to the characters verbosity score according to ptype. 
    '''

    filler = '' 
    num = random.randint(0,10)
    if num > 7: 
        filler = " " + random.choice(RANDOM_FILLER)
        character.add_to_score(verbosity_cal(character, filler, char_ptype))
    return filler 

def generate_ack_ptype(character, p_type): 
    '''
    Input: character, str
    Output: string
    Purpose: This function returns a string acknowledgement based on personality type of character.  
    '''
    
    if p_type == 'introvert': 
        ack = random.choice(INTROVERT_ACK)
    else: #extrovert
        ack = random.choice(EXTROVERT_ACK)

    return ack

def generate_setting_text(): 
    '''
    Input: none 
    Output: string
    Purpose: This function returns a string with setting info.  
    '''
    setting_details = generate_setting()
    setting = setting_details[1] + " " + setting_details[2].upper() + " - " + setting_details[0].upper()

    # State the setting.
    setting_string = '{0:<100}'.format(setting)

    return setting_string

def generate_dialogue_text(character_A, character_B): 
    '''
    Input: 2 characters
    Output: list of str
    Purpose: This function returns a list of dialogue between characters A and B.  
    '''

    # Generate Dialogue.
    dialogue = [] 
    # Greeting 
    dialogue.append(generate_greeting_dialogue(character_A, character_B))

    # A attempts objective 
    dialogue.append(generate_obj_attempt_dialogue(character_A, character_B))

    # B attempts objective 
    dialogue.append(generate_obj_attempt_dialogue(character_B, character_A))

    # Goodbyes 
    dialogue.append(generate_goodbye(character_A, character_B))

    return dialogue

def add_scene_to_play_score(play, character_A, character_B): 
    '''
    Input: play, 2 characters
    Output: none
    Purpose: This function add characters to play and their scores to the play's total score.  
    '''
    play.addCharacter(character_A)
    play.addCharacter(character_B)
    score = character_A.get_score()
    score += character_B.get_score()
    play.add_to_score(score)

def generate_scene(play):
    '''
    Input: 2 characters 
    Output: str
    Purpose: This function generates a scene of dialogue between 2 characters in a setting. 
    
    Each scene should have a: 
        Greeting / small talk 
        A attempts objective 
        B attempts objective 
        Goodbyes 

    '''
    

    try:
        lines = []
        #Setting 
        setting_string = generate_setting_text()
        lines.append(setting_string)

        # Create 2 characters and give them objectives. This is vinette style, so none of the characters have 
        # through plots. (AKA even if names are used multiple times, they are different characters.)
        # This also gives them rough Q&As' for each other
        character_A, character_B = pick_characters_and_objectives()

        # Describe the scene.
        lines.append('{0:<100}'.format(generate_scene_description(character_A, character_B)))

        
        # Generate Dialogue.
        dialogue = generate_dialogue_text(character_A, character_B)

        lines.append('\n\n'.join(dialogue))
        
        #scoring
        add_scene_to_play_score(play, character_A, character_B)
        
        return '\n\n\n'.join(lines)
    except: 
        lines.append('{0:<100}'.format("Silence. They do not move.")) # Make Godot joke 
        print("Error in dialogue generation")
        return ''   

def generate_play(play):
    '''
    Input: str
    Output: none
    Purpose: This generates a screen play of dialogue. 
    '''


    lines = []
    #choose number of scenes 
    num_scenes = random.randint(MIN_NUMBER_SCENES, MAX_NUMBER_SCENES)
    play.add_to_score(num_scenes*4) #add points for numb scenes 

    lines.append('{0:^100}'.format("* * * Talk of the Quad * * *"))
    lines.append('{0:^100}'.format("* * * written by A Little Bird * * *\n"))

    for scene in range(num_scenes):
        scene_lines = generate_scene(play)
        lines.append(scene_lines)

    lines.append('{0:^100}'.format("FIN"))

    return lines 

def generate_play_file(plays, winning_play_index, filename):
    '''
    Input: play, int, str
    Output: none
    Purpose: This method writes a screenplay to a file (filename). 
    '''

    play = plays[winning_play_index]
    
    lines = play.get_text() 

    f= open(filename,"w+")
    for i in lines: 
        f.write(i)
    f.close()  

def main(filename): 
    '''
    Input: filename
    Output: none
    Purpose: This method calls generate paly which writes a screenplay to a file (filename). 
    '''

    winning_play_score = -1
    winning_play_index = 0
    plays = []

    for index in range(NUM_PLAYS): # make several plays, pick the best
        play = PlayClass.Play(index)

        #run algorithm to make & eval play 
        text = generate_play(play)
        play.set_text(text)

        plays.append(play)

        #Check to see if this is currently best play
        if play.get_score() > winning_play_score: 
            winning_play_index = index 
            winning_play_score = play.get_score()

    print("Play number " + str(winning_play_index) + " won!!")
    
    generate_play_file(plays, winning_play_index, filename)

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)