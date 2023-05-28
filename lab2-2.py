r=True
listt=list([])
inp=input("enter a number: ")
while inp!="done":
    if inp.isdigit():
        listt.append(int(inp))
    else:
        print("please enter a number not any other character")
    inp=input("enter a number: ")
print("total: ", len(listt))
print("sum: ",sum(listt))
print("average: ",sum(listt)/len(listt))