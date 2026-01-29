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

## CPU Bound Tasks: Processes which requires more CPU time, spends more time in the running state.
## I/O Bound Tasks: Processes which requires more I/O time, spends mosre time in waiting state.
'''
- CPU is much faster than i/o devices, so if a process starts doing i/o, so CPU should not sit idle and it must be provided with some other process to optimally utilize it.

- States of a Process:
    1.New 2.Ready 3.Running 4.Blocked/Waiting 5.Exit/Terminate

- Multiprogramming: Keeping multiple programs in the main memory at the same time, ready for execution.

- Multiprocessing: A computer using multiple CPUs at one time.

** Multiprocessing and Multithreading are the ways to achieve multitasking.

- Multitasking: RUnning multiple tasks(application) on CPU at one time. CPU shares it memory among them and Requires context switching.

- Multithreading: A technique where process is divided into smaller execution units called threads, which runs concurrently. Multithreading allows multiple threads to share CPU memory, I/o resources at of a single process.
    - - Multithreading is achieved by concurrency, not parallelism.




'''

