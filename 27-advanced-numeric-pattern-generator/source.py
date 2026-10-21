# Case 27: Advanced Numeric Pattern Generator
n=int(input("Half-height (1-6): "))
if n<1 or n>6: print("Invalid size")
else:
    for row in range(1,n+1):
        print(" "*(n-row),end="")
        for x in range(1,row+1): print(x,end="")
        for x in range(row-1,0,-1): print(x,end="")
        print()
    for row in range(n-1,0,-1):
        print(" "*(n-row),end="")
        for x in range(1,row+1): print(x,end="")
        for x in range(row-1,0,-1): print(x,end="")
        print()
