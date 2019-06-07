import sys
#Number of Countries 
N = int(input())
s = set()

for i in range(1,N+1):
    aux = input()
    s.add(str(aux))
#print the size of the set
print(len(s))
