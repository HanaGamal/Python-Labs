def fun(length,start):
    listt=list([])
    index=0
    while index <length:
        listt.append(start)
        start+=1
        index+=1
    return listt

def fun2(num):
    if num%3==0:
        if num%5==0:
            return "FizzBuzz"
        else:
            return "Fizz"
    elif num%5==0:
        return "Buzz"

def fun3():
    word=input("enter word to reverse: ")
    rev=""
    return word[::-1]


def func4(string):
    longest_substring = ""
    current_substring = ""

    for i in range(len(string)):
        if i == 0 or string[i] >= string[i - 1]:
            current_substring += string[i]
        else:
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            current_substring = string[i]
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring
    return longest_substring

arr=fun(10,10)
print(arr)
print(fun2(21))
print(fun3())

st=input("enter a string: ")
print(func4(st))
name=input("please enter your name: ")
if name and name.isalpha():
    email=input("enter your email: ")

    print(name)
    print(email)
