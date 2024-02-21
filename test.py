f = open('test.rle',"r")
s = ''
while True:
    l = f.readline()
    if l == '':             # Empty indicates end of file. An empty line would be '\n'
        break
    if l[0] =='#':
        continue
    if l[0] =='x':
        continue
    s = s + l[:-1]   # To remove EOL
f.close()
print(s)
lst = []
currentFloor = []
nbr = 1
for a in s:
    if a == "$":
        lst.append([currentFloor])
        currentFloor = []
    elif a == 'b':
            currentFloor += [0 for _ in range(nbr)]
            nbr=1
    elif a == 'o':
            currentFloor += [1 for _ in range(nbr)]
            nbr=1
    else:
        nbr = int(str(nbr)+a)
lst.append([currentFloor])
print(lst)