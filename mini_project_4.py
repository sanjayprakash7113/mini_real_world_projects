a={"sun":10000, "tus":212, "wed":5443, "thu":4332, "fri":3232, "sat":12000}
b=0
c=[]
for i in a.values():
    b=b+i
    c.append(i)
print("total expence in this week",b)
print(max(c))
print(min(c))


total = input("Enter purchase amount: ")

if total.isdigit():
    total = int(total)

    if total < 500:
        print("No discount")
        print("Final amount:", total)

    elif 500 <= total < 1000:
        discount = total * 0.05
        final_amount = total - discount
        print("5% discount applied")
        print("Final amount:", final_amount)

    else:
        discount = total * 0.10
        final_amount = total - discount
        print("10% discount applied")
        print("Final amount:", final_amount)

else:
    print("Invalid input")

