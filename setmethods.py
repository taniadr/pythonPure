#This is the shit! #Starting to use the string handlers from scratch and from simplest , let`s see

import re

setSize = int(input())
setElements = input() #will come as a string!!

setElementsInt = re.split(r'[\s]\s*', setElements)
setV = set()
while (setElementsInt) :
    setV.add(int(setElementsInt.pop()))

numberOfQueries = int(input())

for _ in range(0, numberOfQueries) : #here we need another split
    setOperation = input()
    setOperation = re.split(r'[\s]\s*', setOperation)
    if (setOperation[0] == 'pop') :
        setV.pop()
    else :
        if (setOperation[0] == 'remove') :
            setV.remove(int(setOperation[1]))
        else :
            setV.discard(int(setOperation[1]))

print(sum(setV))



