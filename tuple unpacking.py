julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
name, surname, birth_year, movie, movie_year, profession, birth_place = julia

#########
(a, b, c, d) = (1, 2, 3) # ValueError: need more than 3 values to unpack

#########
def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(z)) # this line causes an error
print(add(*z)) # correct unpacking of the tuple

##########
# Dictionary unpacking in a form of tuple
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
for p in pokemon.items():
  print("key: {}, value: {}".format(p[0],p[1])) # here p is treated as tuples of key, value pairs

for key,value in pokemon.items():
  print("key: {}, value: {}".format(key,value)) # key, value are extracted here inside the for loop condition
