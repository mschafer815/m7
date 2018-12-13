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
**Name the filename.txt what ever you want to name the screen play file** --> this will be stored in same directory as 
rest of files 


System Architecture: A more detailed account of your system (at least 4 paragraphs) and its components. 
You should clearly describe what components of script generation that you chose to focus on (e.g., agent 
personality modeling, dialogue generation, narrative prose generation, suspense modeling, conflict modeling, 
musical lyric generation, humor and sarcasm modeling, visual animation, computational cinematography…), 
citing scholarly work as appropriate. Include a block diagram of your system architecture

    "A Little Bird" is play generation system that explored dialogue generation through creating duet 
scenes between "extroverts" and "introverts." When I first set out to write a program that wrote 
screenplays, I was very nervous about the dialogue component. Because of this, I decided to dive 
in and test out some dialogue generation. My screen play generating system is mainly inspire by 
Francois Mairesse and Marilyn Walker's PERSONAGE: Personality Generation for Dialogue paper, where they 
discuss the different sytntaxes, habits, lexicons and speech mannerisms of extroverts vs. introverts. 
In their paper they discuss the many small and large ways introvert and extroverts differ in their speech. 
In their experiment, they would rate sentences / responses based on how extroverted or introverted the styleo 
of the language was and assign it a value. According to their research, Introverts tend to lean towards problem 
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
for the purposes of my system, I choose to stick to 2 personalities type: extrovert and introvert. 


PP2 
This is how my system works 

PP3 
How I would add the evaluation model 

PP4 
What else I would improve



Computational Creativity: You should follow the general SPECS procedure to evaluate your system. Start by 
stating your assumptions and definitions for what it means for a system to be creative here. These statements
should be founded on prior work (i.e., you should be citing respected scholars in the field). Next, clearly 
state at least one creativity metric for your system and evaluate it based on that metric. This metric can 
be derived from the SPECS themes, Ritchie's criteria, the Four PPPPerspectives, or another formalized evaluation
procedure from scholarly work (e.g. Colton's Creative Tripod). Regardless of the metric and definitions you 
specify, you must acknowledge any limitations, biases, or potential issues with your evaluation. Your grade 
will not be affected if your data is biased or limited unless you leave out this information.

Novelty: Novelty and originality - a new product, or doing something in a new way, or seeing new links and 
relations between previously unassociated concepts
Social Interation and Communication: 
Communicating and promoting work to others in a persuasive, positive manner.
Mutual influence, feedback, sharing and collaboration between society and individual.
Generation of Results: Working towards some end target, or goal, or result.
Producing something (tangible or intangible) that previously did not exist.
Domain Competence: Domain-specific intelligence, knowledge, talent, skills, experience and expertise.
Knowing a domain well enough to be equipped to recognise gaps, needs or problems that need solving and to generate, 
validate, develop and promote new ideas in that domain.

Personal Challenges: Describe how you personally challenged yourself on this assignment as a computer scientist. 
How did you strive to make your system unique, meaningful, and use sophisticated techniques? How did you push 
yourself as a scholar and a programmer? What new techniques did you try? What discoveries and connections did 
you make?
This project was quite the beast for me. I picked dialogue generation because that was what I knew the 
least about and frankly what scared me the most. 