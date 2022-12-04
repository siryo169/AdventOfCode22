f = open("./text1.txt")
total= 0
for x in f:
    a = x.split(",")[0].split("-")
    b = x.split(",")[1].split("-")
    if (int(a[0]) >= int(b[0])) and (int(a[1]) <= int(b[1])):
        total+=1
    elif (int(a[0]) <= int(b[0])) and (int(a[1]) >= int(b[1])):
        total+=1

print(total)
f.close()

#problema 2

f = open("./text1.txt")
total= 0
for x in f:
    a = x.split(",")[0].split("-")
    b = x.split(",")[1].split("-")
    if (int(a[0]) <= int(b[0])) and (int(b[0]) <= int(a[1])):
        total+=1
    elif (int(b[0]) <= int(a[0])) and (int(a[0]) <= int(b[1])):
        total+=1

print(total)
f.close()