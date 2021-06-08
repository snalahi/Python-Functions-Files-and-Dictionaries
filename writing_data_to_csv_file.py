# The following method includes .format() methd to write in a csv file. Otherwise .join() method can be used on ',' when all the elements are string 
# and there is no extra comma in between a chunk of string. Follow the code below:
olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    ### .join() method:
    # row_string = ','.join(olympian[0], str(olympian[1]), olympian[2])
    ### concatenation method:
    #row_string = olympian[0] + ',' + olympian[1] + ',' + olympian[2]
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

### OUTPUT ###
# Name,Age,Sport
# John Aalberg,31,Cross Country Skiing
# Minna Maarit Aalto,30,Sailing
# Win Valdemar Aaltonen,54,Art Competitions
# Wakako Abe,18,Cycling

####################_______________________________##########################

# Now, if there remains any other delimiter in any of the elements of olympians list, then we need to consider each element independently within 
# whole block of outfile and row_string. That can be accomplished by this format '" ", " ", " "'. See the following block of code and the OUTPUT for
# clarification.
olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv", "w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

### OUTPUT ###
# "Name","Age","Sport"
# "John Aalberg", "31", "Cross Country Skiing, 15KM"
# "Minna Maarit Aalto", "30", "Sailing"
# "Win Valdemar Aaltonen", "54", "Art Competitions"
# "Wakako Abe", "18", "Cycling"


