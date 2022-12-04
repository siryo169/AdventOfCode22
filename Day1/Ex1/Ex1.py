f = open("./text.txt")
max1 = 0
max2 = 0
max3 = 0 
current = 0
for x in f:
    if x != "\n":
        current += int(x.strip("\n"))
    else:
        
        if current > max1:
            max3 = max2
            max2 = max1
            max1 = current
            
        else:
            if current > max2:
                max3 = max2
                max2 = current
                
            else:
                if current > max3:
                    max3 = current
        current = 0
                    
max = max1 + max2 +max3      
print(max)