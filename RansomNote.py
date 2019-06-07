import re
dic = {} #dictionary

def countingWords(magazineSet,noteSet) :
    magazineSet = re.split(r'[\s]\s*', magazineSet)
    noteSet = re.split(r'[\s]\s*', noteSet)
    for x in noteSet :
        if x not in dic :
            dic[x] = 0
        dic[x] += 1
    for x in magazineSet :
        if x in dic :
            dic[x] -= 1
            if dic[x] == 0 :
                del dic[x]
                if not dic :     #if the dic is empty
                    return True
    return False

setsSize = input()
magazine = input()
note = input()

if (countingWords(magazine,note)) :
    print("Yes")
else :
    print("No")