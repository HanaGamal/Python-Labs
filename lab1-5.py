locations=([])
string=input("enter a string: ")

for index,char in enumerate(string.lower()):
    if char=='i':
        locations.append(index)
if locations:
    print(locations)
else:
    print("letter i is not found")
