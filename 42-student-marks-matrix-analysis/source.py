# Case 42: Student Marks Matrix Analysis
students=["Asha","Bala","Charan","Divya"]; subjects=["Python","Maths","Physics"]
marks=[[88,76,91],[64,72,69],[45,54,48],[92,85,89]]
top=0; topavg=-1
for r in range(len(marks)):
    total=0
    for c in range(len(subjects)): total+=marks[r][c]
    avg=total/len(subjects); print(students[r],total,avg)
    if avg>topavg: top=r; topavg=avg
print("Top",students[top],topavg)
for c in range(len(subjects)):
    total=0
    for r in range(len(marks)): total+=marks[r][c]
    avg=total/len(marks); print(subjects[c],avg)
    if avg<50: print("Low average")
