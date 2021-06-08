fname = 'mydata.txt'
with open(fname, 'r') as md:
    for line in md:
        print(line)
# continue on with other code
fname = 'mydata2.txt'
with open(fname, 'w') as wr:
    for i in range (20):
        wr.write(str(i) + '\n')
