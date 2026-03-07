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

print(num_of_pass_name)
