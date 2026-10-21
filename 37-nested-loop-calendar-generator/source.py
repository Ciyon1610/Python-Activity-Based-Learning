# Case 37: Nested Loop Calendar Generator
start=int(input("First weekday (0-6): "))
days=int(input("Days (28-31): "))
if start<0 or start>6 or days<28 or days>31: print("Invalid calendar input")
else:
    print("Sun Mon Tue Wed Thu Fri Sat")
    date=1; week=0
    while date<=days:
        for day in range(7):
            if week==0 and day<start: print("    ",end="")
            elif date<=days: print(str(date).rjust(3),end=" "); date+=1
            else: print("    ",end="")
        print(); week+=1
