import sys

def printSeq(N):
    for i in range(1,N+1): 
       sys.stdout.write(str(i))

N = int(input())
printSeq(N)