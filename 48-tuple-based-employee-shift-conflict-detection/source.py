# Case 48: Tuple-Based Employee Shift Conflict Detection
shifts=[("Asha",540,720),("Bala",600,780),("Asha",690,810),("Asha",810,900)]
count=0
for i in range(len(shifts)):
    for j in range(i+1,len(shifts)):
        a=shifts[i]; b=shifts[j]
        if a[0]==b[0] and a[1]<b[2] and b[1]<a[2]:
            print("Conflict",a[0],a[1],a[2],b[1],b[2]); count+=1
if count==0: print("No conflicts")
else: print("Total",count)
