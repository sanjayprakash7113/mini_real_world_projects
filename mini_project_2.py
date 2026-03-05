a=["victor","sam","ram"]
b=["sam","ashly","alish","adolph","victor"]
for i in a:
    if i in b:
        print("welcom the party",i)
    else:
        print("your invitasion not acceptable",i)



a=["book1","book2","book3","book4","book5","book6","book7","book8","book9","book10"]
b=["book1","book2","book3","book4","book5","book6","book66"]
for i in b:
    if i in  a:
        print("available",i)
    else:
        print("not available",i)


a=["victor","sam","ram","sam","ashly","alish","adolph","victor"]
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)


a={"victor":100,"sam_s":97,"ram":0,"sam":98,"ashly":99,"alish":45,"adolph":39,"victor_p":90}
num_of_pass=0
num_of_pass_name=[]
num_of_fail=0
num_of_fail_name=[]
for i in a:
    if a[i]>=45:
        num_of_pass+=1
        num_of_pass_name.append(i)
    else:
        num_of_fail+=1
        num_of_fail_name.append(i)
print(num_of_pass)
print(num_of_pass_name)

        
        
        
        
