student_id=[1001,1003,1004,1005,1006,1007,1008]
time=int(input())
attence=[]
for i in student_id:
    if i not in attence and time<9:
        attence.append(i)
    else:
        print(i,"absent today")
print(len(attence),"total precent")


student_attence={1001:8,1003:9,1004:9,1005:8,1006:9,1007:8,1008:9}
present=[]
absent=[]
for student,time in student_attence.items():
    if time<9:
        present.append(student)
    else:
        absent.append(student)
print("total num of present", len(present))
print("absent",absent)



sale1=int(input())
sale2=int(input())
sale3=int(input())
sale4=int(input())
b=0
for i in sale1,sale2,sale3,sale4:
    if i>0:
        b=b+i
    else:
        pass
print("total sale today",b)
        
