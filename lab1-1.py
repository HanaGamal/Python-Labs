vowels=['a','e','i','o','u']
count=0
string=input("enter a string: ")
for i in string:
    if i.lower() in vowels:
        count+=1

if count ==0:
    print("no vowels")
else:
    print("the number of vowels is ", count)
