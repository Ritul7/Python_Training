# Q1.
'''
a=5
b=10

print(a,b)

a = b+a     #a=15
b = a-b     #b=5
a = a-b     #a=10

print(a,b)
'''

#Q2.
'''
print("Enter name: ")
name = input()
print("Enter age: ")
age = int(input())

print(f"My name is {name}, and age is {age}")
'''

#Q3.
'''
num = int(input("Enter a num: "))
if (num%2 == 0):
    print("Even")
else:
    print("Odd")
'''

#Q4.
'''
str1 = input("String1: ")
length = len(str1)

rev = str1[::-1]

if (str1 == rev):
    print("Palindrome")
else:
    print('Not a palindrome')
'''

#Q6
# str = "abababdusunoaifciuo"
# count_dict = {}

# for ch in str:
#     count_dict[ch] = count_dict.get(ch,0) + 1

# print(count_dict)

#Q7

# name = "ritul"
# a = 22
# marks = 32.13

# print("My name is %s and my age is %d, I got %.3f marks" %(name,a,marks))

#

# CLI Calculator

num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))
opt = input("Enter the operation: ")

if(opt == '+'):
    print("Ans is: ", num1+num2)
elif (opt == '-'):
    print("Ans is: ", num1-num2)
elif (opt == '*'):
    print("Ans is: ", num1*num2)
elif (opt == '/'):
    print("Ans is: ", num1/num2)
elif (opt == '//'):
    print("Ans is: ", num1//num2)
elif (opt == '%'):
    print("Ans is: ", num1%num2)
else:
    print("Input Invalid")





    # Dynamic typing
    # CPU bound tasks
    # i/o tasks
    # Multitasking, multiprocessing, multithreading
    # sys module
    # Pyenv
    # CLA (arguments)


