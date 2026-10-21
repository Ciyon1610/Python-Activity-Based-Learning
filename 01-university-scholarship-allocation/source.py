# Case 1: University Scholarship Allocation
records=[("Asha",88,70,92,250000),("Bala",82,65,95,220000),("Charan",76,61,80,310000),("Divya",88,68,92,240000)]
eligible=[]
for name,agg,sub,att,income in records:
    why=[]
    if agg<75: why.append("aggregate")
    if sub<60: why.append("subject minimum")
    if att<75: why.append("attendance")
    if income>300000: why.append("income")
    if len(why)==0: eligible.append((name,agg,att,income))
    else: print(name,"rejected:",", ".join(why))
for i in range(len(eligible)):
    for j in range(len(eligible)-i-1):
        a=eligible[j]; b=eligible[j+1]
        swap=a[1]<b[1] or (a[1]==b[1] and a[2]<b[2]) or (a[1]==b[1] and a[2]==b[2] and a[3]>b[3])
        if swap: eligible[j],eligible[j+1]=eligible[j+1],eligible[j]
print("Ranking")
rank=1
for row in eligible: print(rank,row[0],row[1],row[2],row[3]); rank+=1
