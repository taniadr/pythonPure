def caracterization(num1):
    if n%2 != 0:
        return "Weird"
    else:
     if n >= 2 and n <= 5:
            return "Not Weird"
     else:
         if n >= 6 and n <= 20:
            return "Weird"
         else:
             if n > 20: 
                return "Not Weird"

n = int(input())
res = caracterization(n)
print(res)