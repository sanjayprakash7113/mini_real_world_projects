raw=input("")
raw=raw.replace(","," ")

visitors=raw.split()
total_visitors=len(visitors)
b={}
for i in visitors:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
repet_visitors=[]
for i in b:
    if b[i]>=1:
        repet_visitors.append(i)
print(b)
print(total_visitors)


expence={"food":100,"travel":40,"shoping":1000,"snacks":40}

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
