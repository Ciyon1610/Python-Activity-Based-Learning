# Case 55: Tuple-Based Transaction Audit
tx=[("T101",1200,"deposit"),("T102",6500,"withdrawal"),("T103",7200,"withdrawal"),("T102",300,"deposit"),("T104",-50,"withdrawal")]
for i in range(len(tx)):
    tid=tx[i][0]; amount=tx[i][1]; kind=tx[i][2]
    if amount<=0: print("Invalid amount",tid,amount)
    if kind!="deposit" and kind!="withdrawal": print("Invalid type",tid)
    for j in range(i+1,len(tx)):
        if tid==tx[j][0]: print("Duplicate ID",tid)
streak=0
for tid,amount,kind in tx:
    if kind=="withdrawal" and amount>5000:
        streak+=1
        if streak==2: print("Suspicious consecutive large withdrawals")
    else: streak=0
