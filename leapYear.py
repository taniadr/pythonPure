def isLeapYear(year):    
    if year % 4 == 0:
        if year % 100:
            if year % 400 == 0:
                return True
    return "False"
y = int(input())

if isLeapYear(y): 
    print("True")
else:
    print("False")