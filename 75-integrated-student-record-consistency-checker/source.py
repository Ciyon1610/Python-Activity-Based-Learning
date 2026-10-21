# Case 75: Integrated Student Record Consistency Checker
records=[("24CS101","Asha Rao",86,91),("24CS101","Bala Das",72,78),("24M2102"," ",104,65),("24EC103","Charan Dev",68,-2)]
for i in range(len(records)):
    sid=records[i][0]; name=records[i][1]; marks=records[i][2]; att=records[i][3]
    errors=[]; ok=len(sid)==7
    if ok:
        for p in range(2):
            if not ("0"<=sid[p]<="9"): ok=False
        for p in range(2,4):
            if not ("A"<=sid[p]<="Z"): ok=False
        for p in range(4,7):
            if not ("0"<=sid[p]<="9"): ok=False
    if not ok: errors.append("malformed ID")
    for j in range(i+1,len(records)):
        if sid==records[j][0]: errors.append("duplicate ID"); break
    if name.strip()=="": errors.append("blank name")
    if marks<0 or marks>100: errors.append("invalid marks")
    if att<0 or att>100: errors.append("invalid attendance")
    if len(errors)==0: print(sid,"VALID")
    else: print(sid,", ".join(errors))
