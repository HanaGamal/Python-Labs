listt=([])
for i in range(5):
    x=input("enter number: ")
    listt.append(x)
sorts=sorted(listt)
print(sorts)
sorts.reverse()
print(sorts)