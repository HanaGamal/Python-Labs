num=int(input("enter a number: "))
table=[]

for i in range(num):
    row=[]

    for j in range(i+1):

        row.append((j+1)*(i+1))
    table.append(row)

print(table)