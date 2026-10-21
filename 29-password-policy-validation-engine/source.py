# Case 29: Password Policy Validation Engine
p=input("Sample password: ")
u=l=d=s=space=repeat=False
symbols="!@#$%&"
for i in range(len(p)):
    c=p[i]
    if "A"<=c<="Z": u=True
    if "a"<=c<="z": l=True
    if "0"<=c<="9": d=True
    if c in symbols: s=True
    if c==" ": space=True
    if i>0 and c==p[i-1]: repeat=True
checks=[("length",len(p)>=8),("uppercase",u),("lowercase",l),("digit",d),("symbol",s),("no spaces",not space),("no repeats",not repeat)]
valid=True
for label,ok in checks:
    if ok: print("PASS",label)
    else: print("FAIL",label); valid=False
if valid: print("Valid")
else: print("Invalid")
