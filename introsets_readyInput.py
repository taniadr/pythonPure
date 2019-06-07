def average(array):
    v = set()
    for x in array :
        v.add(x)
    return (float(sum(v)/len(v)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)