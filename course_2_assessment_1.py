# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and
# save to the variable num.
travel_file = open('travel_plans.txt', 'r')
num = len(travel_file.read())


# We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and
# assign this value to the variable num_words.
emo_file = open('emotion_words.txt', 'r')
num_words = len(emo_file.read().split())


# Assign to the variable num_lines the number of lines in the file school_prompt.txt.
sc_file = open('school_prompt.txt', 'r')
num_lines = len(sc_file.readlines())


# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
sc_file = open('school_prompt.txt', 'r')
beginning_chars = str(sc_file.read().strip()[:30])


# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
sc_file = open('school_prompt.txt', 'r')
lines = sc_file.readlines()
three = []
for l in lines:
    three.append(l.split()[2])

    
# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
emo_file = open('emotion_words.txt', 'r')
lines = emo_file.readlines()
emotions = []
for l in lines:
    emotions.append(l.split()[0])

    
# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
tr_file = open('travel_plans.txt', 'r')
all_text = tr_file.read()
first_chars = ''
for ch in all_text[:33]:
    first_chars += ch

    
# Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
sc_file = open('school_prompt.txt', 'r')
lines = sc_file.read().split()
p_words = []
for l in lines:
    if l.__contains__('p'):
        p_words.append(l)
