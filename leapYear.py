year=int(input("Enter a year: "))
for y in [year,2000,2004,2015,2016]:
    if y % 4 == 0 :
        print(f"{y} is a leap year")
    elif y % 100 == 0 :
        print(f"{y} is a not leap year")
    elif y % 400 == 0 : 
        print(f"{y} is a leap year")  
    else:
        print(f"{y} is not a leap year") 