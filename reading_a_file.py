fileref = open("olympics.txt", "r")
## Mind it the file should be in the same folder of the program execution.
lines = fileref.readlines()
print(len(lines))
total_char = 0
for line in lines:
    total_char += len(line)
    print(line.strip())
print(total_char)
fileref.close()

