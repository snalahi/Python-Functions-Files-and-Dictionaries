fileref = open("olympics.txt", "r")
## Mid it the file should be in th
lines = fileref.readlines()
print(len(lines))
total_char = 0
for line in lines:
    total_char += len(line)
    print(line.strip())
print(total_char)
fileref.close()
