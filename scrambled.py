import random
f = open("C:\\Users\\Admin\\Documents\\my doc\\sample.txt","r")
f1 = open("C:\\Users\\Admin\\Documents\\my doc\\samplescrambled.txt","w")
newone = f.read()
word1 = newone.split()
for i in word1 :
    if len(i) <= 3 :
        f1.write(i)
        f1.write(" ")

    else :
        data = i[1:-1]
        we = list(data)
        random.shuffle(we)
        words = "".join(i[0]) + "".join(we) + "".join(i[-1])
        f1.write(words)
        f1.write(" ")

f.close()
//thanks
f1.close()
