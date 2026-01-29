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

