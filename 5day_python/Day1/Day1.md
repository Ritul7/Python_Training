# DAY 1: Python Basics and Env Setup

## Identity Operators:- 

- 1. is: Small integers(-5 to 256) are pre-created, to improve performances, this is called integer interning (caching).
- - Therefore, a=4, b=4, print(a is b) returns true as they are same object
- - a = ["app", "jf"], b = ["app", "jf"], print(a is b) returns false as they are different object, python always creates a new list every time.

- is vs == : "is" is for identity(same memory object), "==" is for equality(same value).

### Imp:-
- Immutable objects(str, int, tup) can share same memory, python can reuse them
- Mutable objects(lists, dict, set) are always created new.

## 2. Membership Operators:-

- 1. in: Checks the membership(existance) of a value in a sequence.
- operator.contains() method acts like 'in' operator. 

## 3. Python Strings:-

- Sequence of characters. Are immutable i.e. always returns a new string after manipulaiton

### Methods in string:-

1. Slicing - Using ':' operator, using slice()
- - str[::-1]- Reverse the string
- - str[::-2]- Reverse the string and skip one character
 
2. strip() - Removes the leading and trailing whitespaces, new line characters(\n) and tab characters(\t).
- - strip(chars) - Removes every occurrence of the 'chars' in string

3. uppercase() - All char to Uppercase, lowercase() - All char to lowercase

4. title() - Capitalize first char of each word 

5. split() - "String into List"
- - Based on some delimeter
- - Ex: print(str.split(`seperator`))
- - str.split(`seperator`,`maxsplit`)

- - list(a), b = [*s] <-"Unpacking operator" ...They are used to convert a string into list(char by char)

6. join() - Uses a seperator and iterable to make them a single string. join() only works on iterables containing strings. If data other than string, gives error.
- - "seperator".join(iterable)

- join joins keys of dictionary
- sets are unordered, to output is different

7. replace(), find()

## 4. String Formatting:-

- Inserting variables and expressions into strings to make the output dynamic.
- % operator
- .format()
- f-string
- Formatting specifier - .2f. Here f represents floating number and 2 describes the 2 digits after decimal

## 5. CPU Bound Tasks: 
- Processes which requires more CPU time, spends more time in the running state.
- I/O Bound Tasks: Processes which requires more I/O time, spends mosre time in waiting state.

- CPU is much faster than i/o devices, so if a process starts doing i/o, so CPU should not sit idle and it must be provided with some other process to optimally utilize it.

- States of a Process:
    1.New 2.Ready 3.Running 4.Blocked/Waiting 5.Exit/Terminate

- Multiprogramming: Keeping multiple programs in the main memory at the same time, ready for execution.

- Multiprocessing: A computer using multiple CPUs at one time.

### Multiprocessing and Multithreading are the ways to achieve multitasking.

- Multitasking: RUnning multiple tasks(application) on CPU at one time. CPU shares it memory among them and Requires context switching.

- Multithreading: A technique where process is divided into smaller execution units called threads, which runs concurrently. Multithreading allows multiple threads to share CPU memory, I/o resources at of a single process.
    - - Multithreading is achieved by concurrency, not parallelism.

## 6.GIL:- (Global Interpreter Lock)

- It is mutex(lock) in python that allows only one thread to execute bytecode at a time in CPython.
- WHY GIL? Bcz python uses automatic memory management(reference counting), like a=[]; b=a. Without GIL, two threads might increase ref counting simultaneously.
- Every thread have its own GIL.

### .............. Q. If GIL exists, then how multithreading is achieved?.........
- Multithreading is achieved using concurrency, not by parallelism.

- (Parellelism)- Multiple tasks excute at the exact same time. Requires multiple CPUs. Lile multiprocessing.
- (Concurrency) - Multiple tasks make progress together, but nit necessarily at the same time. One CPU is enough. Only one task run at a timem but both progress.
- Python achieves multithreading by releasing GIL everytime, when the thread is blocked/waiting

## 7.Command Line Arguments:- 

- These are the arguments passed to a script when run from the terminal.
- We use "sys" module to access command line arguments. It gives a list called "sys.argv" which contains everything we write after python3

## 8. sys module:-

- Built-in python module that gives access to sys-specific parameters and functions like CLA.
- Allows interaction with python run-time environment (Ex: path, version, exit)
- Reading input and writing output, sys.stdin, sys.stdout.write("ritul").
- sys.path => It prints all the system paths
- sys.modules() => Dictionary that prints all the modules that are currently imported
- sys.getrefcount() => Gives ref count to an object.

## 9.Pyenv:-
 - Pyenv is a tool used for managing different versions of python in a system.