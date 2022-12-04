f = open("./text.txt")
total = 0
for x in f:
    match x[2]:
        case "X":
            total += 0
            match x[0]:
                case "A":
                    total += 3
                case "B":
                    total += 1
                case "C":
                    total += 2         
        case "Y":
            total += 3
            match x[0]:
                case "A":
                    total += 1
                case "B":
                    total += 2
                case "C":
                    total += 3 

        case "Z":
            total += 6
            match x[0]:
                case "A":
                    total += 2
                case "B":
                    total += 3
                case "C":
                    total += 1 

print (total)