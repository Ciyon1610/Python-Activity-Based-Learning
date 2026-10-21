# Case 47: Sports Tournament Ranking System
teams=[("Falcons",7,5,9),("Tigers",7,3,8),("Eagles",6,4,7),("Wolves",7,5,10)]
for i in range(len(teams)):
    for j in range(len(teams)-i-1):
        a=teams[j]; b=teams[j+1]
        swap=a[1]<b[1] or (a[1]==b[1] and a[2]<b[2]) or (a[1]==b[1] and a[2]==b[2] and a[3]<b[3]) or (a[1:4]==b[1:4] and a[0]>b[0])
        if swap: teams[j],teams[j+1]=teams[j+1],teams[j]
print("Rank Team Points GD Goals")
rank=1
for name,points,gd,goals in teams:
    print(rank,name,points,gd,goals); rank+=1
