#program to check if year is a leap year or not

year = 2000

def leap_year_check(year):
    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               return f"{format(year)} is a leap year"
           else:
               return f"{format(year)} is not a leap year"
       else:
           return f"{format(year)} is a leap year"
    else:
       return f"{format(year)} is not a leap year"
    
print(leap_year_check(year))