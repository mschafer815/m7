# Mackenzie Schafer 
# Last Edit: 12/13/18
# Script Generation Character Objective Object Class 
# Computational Creativity Fall 2018 



class Objective:
    '''
    This class defines character objects. Each character has a statement, and questions. 
    '''


    def __init__(self, statement):
        ''' 
        Input: none
        Output: none
        Purpose: This initializes objective with statement, and question1 and 2'''  
        self.statement = statement
        self.question_answer_list = []

    def get_statement(self): 
        ''' 
        Input: none
        Output: str
        Purpose: Returns statement'''
        return self.statement

    def set_question_and_answers(self, question, answers): 
        ''' 
        Input: str, list of str
        Output: none
        Purpose: This sets the question and its possible answers in the 
        question_answer_list [question, [answers]''' 
        self.question_answer_list.append(question)
        self.question_answer_list.append(answers)

        return self.question_answer_list

    def get_question(self): 
        ''' 
        Input: none
        Output: str
        Purpose: Returns question'''

        return self.question_answer_list[0]

    def get_answer(self, index): 
        ''' 
        Input: none
        Output: str
        Purpose: Returns answer at specified index'''
        return self.question_answer_list[1][index]

    def __str__(self): 
        ''' 
        Input: None
        Output: string
        Purpose: This function returns an informal string version of the object. 
        '''
        if len(self.question_answer_list) == 2: 
            string = ("Statement: " + self.statement + "\nQuestion: " + self.question_answer_list[0] + 
            "\nAnswers: " + str(self.question_answer_list[1])) 
        else: 
            string = "Statement: " + self.statement
        return string

    def __repr__(self): 
        ''' 
        Input: None
        Output: string
        Purpose: This function prints a formal string version of the object. Right now same as __str__ func.  
        '''
        
        if len(self.question_answer_list) == 2: 
            string = ("Statement: " + self.statement + "\nQuestion: " + self.question_answer_list[0] + 
            "\nAnswers: " + str(self.question_answer_list[1])) 
        else: 
            string = "Statement: " + self.statement
        return string


