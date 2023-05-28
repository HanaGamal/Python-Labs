vowels=['a','e','i','o','u']
string=input("enter a word: ")
new=""
for i in string:
    if i in vowels:
        new=string.replace(i,"")
print(new)