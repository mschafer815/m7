Mackenzie Schafer
12/13/18 

Overview: 1 paragraph that describes your system. State the system's name and why it's called so, 
as well as the main components of the system and the algorithms behind them

System name: A Little Bird
Generates Plays named "The Talk of the Quad" 
These plays are vinette style plays inspired by John Cariani's "Almost, Maine" which features 
a series of duet scenes about couples in Almost, Maine. "A Little Bird" is a Bowdoin inspired 
attempt at duet scene generation like that in Almost, Maine. My system focusses on dialogue generation, 
specifically with regards to speech differences between extroverts and introverts. The system 
creates a series of scenes (3-8) each with 2 characters. Each of the characters is assigned 
a variety of qualities (name, hometown, friends, love interest, hobbies, etc.) as well as an objective. 
Each objective is to find out a piece of information about your scene partner. Throughout a scene there is 
a greeting, time for both characters to try to achieve their objective, and a goodbye (depending on whether 
or not they were sucessful in their objective). 


Setup: Step-by-step instructions for how to run your code, including any dependencies, versions, and so on
open up terminal
run the command: 
python3 generateScript.py filename.txt
--> Name the filename.txt what ever you want to name the screen play file** --> this will be stored in same directory as 
rest of files 
--> In terminal you will receive output of possible Error in dialogue generation as well as which 
play won! 

System Architecture: A more detailed account of your system (at least 4 paragraphs) and its components. 
You should clearly describe what components of script generation that you chose to focus on (e.g., agent 
personality modeling, dialogue generation, narrative prose generation, suspense modeling, conflict modeling, 
musical lyric generation, humor and sarcasm modeling, visual animation, computational cinematography…), 
citing scholarly work as appropriate. Include a block diagram of your system architecture

    "A Little Bird" is play generation system that explores dialogue generation through creating duet 
scenes between "extroverts" and "introverts." When I first set out to write a program that wrote 
screenplays, I was very nervous about the dialogue component. Because of this, I decided to dive 
in and test out some dialogue generation. My screen play generating system is mainly inspired by 
Francois Mairesse and Marilyn Walker's PERSONAGE: Personality Generation for Dialogue paper, where they 
discuss the different sytntaxes, habits, lexicons and speech mannerisms of extroverts vs. introverts. 
In their paper they discuss the many small and large ways introverts and extroverts differ in their speech. 
In their experiment, they would rate sentences / responses based on how extroverted or introverted the style 
of the language was and assigned it a value. According to their research, Introverts tend to lean towards problem 
talk, dissatisfaction, and use many negations, while extraverts tend toward pleasure talk, agreement, and 
very few negations. In addition, introverts tend to be very concise and more formal in their speech while 
extroverts are more verbose and redundant. Introvert tend to stay on a single topic and extroverts tended to 
switch topics. Introvert often use what the authors refer to as "Downtoner Hudges" such as 
"sort or, somehwat, I mean, etc." while extroverts use "emphasizer hedges" ("really, basically, just, etc."). 
There are also difference in acknowledgements between introverts and extroverts. While in my other readings, 
this idea of such a hard binary of personality was found to be heavily disputed (although authors such as 
Marc Cavazza and Fred Charles in Dialogue Generation in Character-based Interactive Storytelling and 
Mairesse and Walker in a later paper Using Linguistic Cues for the Automatic Recognition of Personality 
in Conversation and Text). Many of these authors offered up a variet of other personality types and qualities
(noteavly the "Big Five") such as "pursueder", "stability", and "Openess to experience." Hoever, I decided 
for the purposes of my system, I choose to stick to 2 personalities type: extrovert and introvert. I also 
decided to make sure that each character has an objective in the scene and attempts to fufill their objective. 
This is inspire from my work in theater where we are constantly drilled in writing, acting and directing-- 
"What is the character's objective? This determines why they are onstage. What are they trying to get?"

    My system generates 10 plays and picks the play based on the cumulative score of its characters. Each 
play consists of 3-8 scenes. Each scene has a setting, 2 characters, a scene description describing 
the character's objectives for the scenes and the characters' dialogue. Each set of dialogue has a greeting, 
an opportunity for character a to achieve their objective (learn some piece of information about character b), 
an opportunity for character b to achieve their objective (learn some piece of information about character a),
and goodbyes based on personality type and if the character achieved their objective. As each character speaks, 
they can earn points based on verbosity and their personality type. Extroverts get rewarded for longer lines and 
introverts get rewarded for shorter lines. Introverts can also get bonus points for pausing as Marilyn and Mairesse
state introvert are more likely to have many unfilled pauses. Once a scene is generated, its score (character a's score +
character b's score) is added to the overall play score. 

In my system there are 4 classes of code: 
        generateScript.py (the master script generating program)
        CharacterClass.py (defines the character object)
        ObjectiveClass.py (defines the objective object)
        PlayClass.py (defines the play object)
    
    Character Objects: when each character is initialized with a name and objective statement. 
They then have properties (variables): name,  personality type (intovert or extrovert), hometown (randomly choosen from a list of cities), 
interests (randomly choose from a list of hobbies), friends (num of friends range determined by introversion and 
extroversion, names of friends chosen at random from a list of people), love interests (randomly choosen from list of 
people), score (starts at zero, increase by verbosity vs. personality type), objective object, and objective success (bool starts 
at False, change to true if character was successful in obtaining their objective). 

    Obejctive Object: initialized with statement. Vars: statement (str representation of objective), question_answer_list (list 
of [Question to achieve objective, possible answers to question]). As it lies now, when character a goes to achieve its object and ask 
the question, character a asks the question and character b can respond with one of the possible answers. This is a part that I would have 
really like more time to expand on. I think it would be really cool for based on the different personality types to have 
different ways of asking or answering the questions. 

    Play Object: initialized with name (int); vars: name (int), characterList (list of characters), score (int) and text (string). 
This object exists to be able to compare plays to one another. I think this would also be interesting to expand moving beyond 
dialogue because you could change play's score based on other criteria (plot, length, humor, etc.)

Dialogue structure: 
    Greetings: Each character is given a greeting based on their personality type. Some of the greetings are questions. If one 
    character's greeting is a quesiton, when the other character responds they will "I'm " + an adj + punctuation mark. The 
    adj and punct are determined by the character's personality type. Introverts (according the M&M) are more likely to 
    use periods and pause so they can use periods and ... whereas extroverts are use ! and . (but are more likely 
    to choose an !). 

    Character Attempt at Objective: When a character attempts to get information out of their scene partner they can use a few different 
    tactics, depending on their personality type. Becuase extroverts tend to bring up multiple topics, extroverts attempting to 
    accomplish their objective might bring up a side topic before. Introverts on the other hand have the option to Pause. 
    This can happen over an over again until the characters finally asks their question to their scene partner. At this time, 
    the scene partner has a random chance of either answer it or not. If the scene partner answer the character's quesiton, 
    the character's objective_success variable is set to True (which will affect their goodbye later). Otherwise, the scene 
    partner will give some random filler dialogue. Random filler dialogue can happen by chance in a variety of positions 
    throughout the dialogue. Both character A and 

    Goodbye: Each character is given a goodbye based on whether they are an introvert or an extrovert and whether or not they 
    were sucessfull in their objective. Introvert options are less verbose and generally less enthusiastic. Extroverts are 
    more verbose and more upbeat and enthusiastic (as M&M describe as please talk). Extroverts also tend to have more self talk 
    so this is included in their speech as well. 


Further Exploration: 
The biggest improvements I would like to make to this program is in the character scoring. At this point I am only relying on 
verbosity vs. personality type and pause bonuses for introverts. If I had more time I would love to be able to add a text variable 
to the character object and add all of the characters lines to this and then be able to perform analysis on this text and adjust the 
character's overall score accordingly. For example, I would have loved to incorportate how M&M say that extroverts refers to themselves 
more often than introverts (aka give extroverts more points when they say "I" and "You"). I would also like to explore how 
introverts use more negative speech than extroverts by assigning points based on positivity and negativity in word such as 
adjectives, as well as modifiers like "not" and "no". I could also do an overall score for punctuation. I also would like 
to imrpov the question-- answer component. It would be great if you can have multiple questions and answers that corresponded with 
personality types and specific scenarios. I would also like to add a bit to avoid repetition / score it accordingly. 


Computational Creativity: You should follow the general SPECS procedure to evaluate your system. Start by 
stating your assumptions and definitions for what it means for a system to be creative here. These statements
should be founded on prior work (i.e., you should be citing respected scholars in the field). Next, clearly 
state at least one creativity metric for your system and evaluate it based on that metric. This metric can 
be derived from the SPECS themes, Ritchie's criteria, the Four PPPPerspectives, or another formalized evaluation
procedure from scholarly work (e.g. Colton's Creative Tripod). Regardless of the metric and definitions you 
specify, you must acknowledge any limitations, biases, or potential issues with your evaluation. Your grade 
will not be affected if your data is biased or limited unless you leave out this information.

Sources: 
http://www.aaai.org/Papers/JAIR/Vol30/JAIR-3012.pdf
http://www.aaai.org/Papers/AIIDE/2005/AIIDE05-004.pdf 
https://link.springer.com/chapter/10.1007/978-3-540-85483-8_5 
https://link.springer.com/content/pdf/10.1007%2F978-3-540-85483-8.pdf

As mentions before, most of my inspiration and guideance for this project came from Marilyn Walker and 
Francois Mairesse's paper on "PERSONAGE: Personality Generation for Dialogue." 

As for evaluating the creativitiy of this project, thre 3 most important piece of SPEC's criteria I choose were;  
Novetly, Social Interaction and Communication, adn Domain Competence 

Novelty: Novelty and originality - a new product, or doing something in a new way, or seeing new links and 
relations between previously unassociated concepts
-->My program is inpired from M&M's PERSONAGE system focussing on similar attributes of introverts and extroverts 
that these ladies pulled out. However, they were more focussed on analyzing single bits on text whereas my 
implementation of my code creates a scene play of dialogue. I made up the greeting, objective, goodbye structure (although 
I have no way to prove how novel that it). Overall the system creates novel results everytime from the hard 
coded input data and random adjective and punctuation combinations I provided. Some of the acks and sentences were pulled 
directly from examples in M&M's paper. 


Social Interation and Communication: Communicating and promoting work to others in a persuasive, positive manner.
Mutual influence, feedback, sharing and collaboration between society and individual. Generation of Results: Working 
towards some end target, or goal, or result. Producing something (tangible or intangible) that previously did not exist.
-->This system produces a screenplay-- which is a tangible result that did not previously exist! 

Domain Competence: Domain-specific intelligence, knowledge, talent, skills, experience and expertise.
Knowing a domain well enough to be equipped to recognise gaps, needs or problems that need solving and to generate, 
validate, develop and promote new ideas in that domain.
--> Overall this system is pretty low on domain competence because it is only pulling from text options in a hardcoded 
minimal list. Could be improved by incorporating larger database of knowledge of text. 

Personal Challenges: Describe how you personally challenged yourself on this assignment as a computer scientist. 
How did you strive to make your system unique, meaningful, and use sophisticated techniques? How did you push 
yourself as a scholar and a programmer? What new techniques did you try? What discoveries and connections did 
you make?
This project was quite the beast for me. I picked dialogue generation because that was what I knew the 
least about and frankly what scared me the most. This project was a lot of moving parts to tackle. I was really 
interested in the variety of papers I read about personality types affecting language. I challenged myself to 
really think about and figure out how to implement code that needs to tackle a variety of problems at once within dialogue. 
I definitely see this program as a work in progress, but I was really focussed on creating a strudy and robust base 
that I could build on. I wanted to implement things in a way that would allow for things to be easily added/changed 
which took a bit of time. I also really challenged myself to think about how do construct a conversation? What are the 
necessary components? How can you automatize this? I also just have not written this much code by myself on any project 
I don't think. Which is really exciting! I got to built this from the bottom up myself :) 
Overall I really enjoyed this project and want to continue explore work in this area. 