# Case 66: Student Academic Risk Classification
names=["Asha","Bala","Charan","Divya"]; marks=[[55,62,58],[42,46,48],[78,81,75],[65,60,70]]
attendance=[82,68,88,74]; lab=[72,35,64,32]; counts=[0,0,0]
for i in range(len(names)):
    total=0
    for m in marks[i]: total+=m
    avg=total/len(marks[i]); reasons=[]
    if avg<50: reasons.append("marks")
    if attendance[i]<75: reasons.append("attendance")
    if lab[i]<40: reasons.append("lab")
    n=len(reasons)
    if n==0: category="Low"; counts[0]+=1
    elif n==1: category="Moderate"; counts[1]+=1
    else: category="High"; counts[2]+=1
    reason_text=", ".join(reasons)
    if len(reasons)==0: reason_text="no flags"
    print(names[i],avg,category,reason_text)
print("Low Moderate High",counts)
