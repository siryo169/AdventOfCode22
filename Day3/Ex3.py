f = open("./text1.txt")
prior = 0
for x in f:
    y = x[:int((len(x)/2))]
    z = x[(int(len(x)/2)):]
    a = set(y).intersection(z)
    for b in a:
        if b.isupper():
            prior += ord(b) - ord('A') + 27
        else:
            prior += ord(b) - ord('a') + 1
f.close()
print(prior)

#part 2
f = open("./text.txt")
prior = 0
fl = ""
sl = ""
tl = ""
for x in f:
    if fl == "":
        fl = x.strip("\n")
        print(fl)
    else:
        if sl == "":
            sl = x.strip("\n")
            print(sl)
        else:
            if tl == "":
                tl = x.strip("\n")
                print(tl)
                a = (set(fl).intersection(sl)).intersection(tl)
                print(a)
                for b in a:
                    if b.isupper():
                        prior += ord(b) - ord('A') + 27
                    else:
                        prior += ord(b) - ord('a') + 1
                fl = ""
                sl = ""
                tl = ""

print(prior)