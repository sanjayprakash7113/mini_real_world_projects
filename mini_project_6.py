expence={}
while True:
    category=input("enter thr name :")
    if category=="stop":
        break
amount=int(input())
if category in expence:
    expence[category]+=amount
else:
    expence[category]=1
total=0
maxi=0
high_exp=None
for k,v in expence.items():
    total+=v
    if v>maxi:
        maxi=v
        high_exp=k
print(total)
print(high_exp)
