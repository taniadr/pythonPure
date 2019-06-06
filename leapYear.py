# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)

def is_leap(year): 
    res = False  
    if (year % 4 != 0):
        res = False    
    else:
        if (year % 100 != 0):
            res = True
        else:
            if (year % 400 != 0):
                res = False
            else:
                res = True
    return res

year = int(input())
print(is_leap(year))