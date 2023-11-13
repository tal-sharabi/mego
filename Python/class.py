'''
Interpreter vs Compiler (מהדר)

common:
both translate source code into machine code

interpreter: - פרשן
line after line
does not use the RAM for the entire program

examples: Python, JS, PHP, Bash, and more...
main disadvantage: SLOW....

Compiler:
The entire program loads into memory before the program runs

others:
HTML - HyperText Markup Language

use examples:
testing - interpreted
production (MS Office) - compiled languages (C/C++/...)

Java compiler uses bytecode (WORA)

<EOM> / <EOT>


random.shuffle()
gets a list, and shuffles its content (elements)


import random

password = []
letters = ['J', 'o', 'h', 'n']
# appending "something" to the empty password list
# the "something" is a random 'choice' element from the letters list

# password.append(random.choice(letters))
# password.append(random.choice(letters))
# password.append(random.choice(letters))
# password.append(random.choice(letters))
# password.append(random.choice(letters))
password.extend(letters)

# print(f"Before\n{password}") # placeholder or interpolation

random.shuffle(password)  # מביא לו בערבוב
# print(f"\nAfter\n{password}")

# DISCLAIMER!!! the shuffle() method is דורסנית!!!
print(password)
# the shuffle() method does NOT return a new "shuffled" list
# overrides - דורס
# the shuffle() method overrides the original contents of the given list


Functions
--------
קלט -> עיבוד -> פלט

---> input ---> processing (algorithm) ----> output the "new" thing

3 types:
built-in functions
ready functions, using import to use them
our own custom-made functions

define (def)



# def printYourName():
#     print("John")


# function call
# printYourName()

# each function has its own (code)block
# the function block is bounded by indentations (הזחות)
def addTwoNumbers():
    # print(x + y)
    print("Bye now!")


# print("Bye now!")
#addTwoNumbers(5, 10)
# x = 5
# y = 10

# addTwoNumbers(5, 10)
# addTwoNumbers()

x = 21
y = 5

                    # function signature
def tal_is_annoying(x, y):
    print(x + y)


tal_is_annoying(2,3)


# HW:
1. Write a function which gets 3 numbers and prints their multiplication result
2. Write a func. which get 2 inputs: a. first name,  b. family name
   and then write the user full_name.
3. Write a func. which gets 3 numbers from the user and prints the BIGGEST number.
4. write a function which gets 3 student names and prints the one with the longest name.
5. write a func. which accept 1 number from the user and prints if it's even or odd.
6. Write a func. which accepts a radius and returns the area of the circle.
EVERYTHING IS IN THE SAME FILE. I WILL JUST CHOOSE A FUNCTION TO "CALL".
-- YOU DON'T CALL ANYTHINdG!  (don't call me I'll call you)
'''