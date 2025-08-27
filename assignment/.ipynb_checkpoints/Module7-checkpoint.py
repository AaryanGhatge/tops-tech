#  1) What are the types of Applications ?

# Desktop Applications : Installed on a personal computer or laptop (e.g., MS Word, Photoshop).
#Web Applications :Run in a web browser and don’t require installation (e.g., Gmail, Facebook).
# Mobile Applications : Designed for smartphones and tablets (e.g., WhatsApp, Instagram).
# Console Applications : Text-based programs that run in a command-line interface (e.g., command prompt tools).
# Embedded Applications : Software designed to run on specialized hardware like ATMs, washing machines, and smart TV.


#  2) what is programing ?

# Programming is the process of designing and writing instructions that a computer can understand and 
# execute to perform a specific task. These instructions are written in programming languages like Python, 
# C, or Java. It involves problem-solving, logic building, and implementing algorithms to create functional software.


#  3) What is Python?

# Python is a high-level, interpreted, and general-purpose programming language known for its simple syntax and readability.
# It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. 
# Python is widely used for web development, data analysis, artificial intelligence, machine learning, automation, and more. 
# large standard library and community support make it one of the most popular programming languages in the world.

#  4) Write a Python program to check if a number is positive, negative or zero.? 


# Take input from the user
num = float(input("Enter a number: "))

# Check the condition
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")
 

# 5) Write a Python program to get the Factorial number of given numbers. 


# Take input from the user
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")


#  6) Write a Python program to get the Fibonacci series of given range.

# Take number of terms from user
n = int(input("Enter the number of terms: "))

# First two terms
a= 0
b= 1

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# 7)  How memory is managed in Python? 

#  Private Heap Space :–
# All Python objects and data structures are stored in a private heap.
# This heap is managed internally by the Python Memory Manager.

# Memory Manager :–
# Allocates and deallocates memory for objects.
# Works with the garbage collector to free unused memory.

# Garbage Collection :–
# Python uses automatic garbage collection to remove objects that are no longer in use.
# It mainly uses reference counting (tracking how many references point to an object).
# If the count becomes zero, the memory is freed.
# Also uses a cyclic garbage collector to detect and clean up objects involved in reference cycles.

# Dynamic Typing :–
# Memory is allocated dynamically at runtime based on the object type and size.

# 8) What is the purpose continuing statement in python? 

for i in range(5):
    if i == 2:
        continue
    print(i)
# 9) Write python program that swap two number with temp variable and without temp variable. 
 
 # Swap with temp variable
x = int(input("Enter x number: "))
y = int(input("Enter y number: "))

temp = x
x = y
y = temp
print(f"After swapping (with temp):x={x} and y={y}")

# 10) Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user. 
  

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is odd.")


 # 11) Write a Python program to test whether a passed letter is a vowel or not.



letter = input("Enter a letter: ").lower()  # Take input as string and convert to lowercase

if letter in ['a', 'e', 'i', 'o', 'u']:
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is not a vowel.")


#  12)  Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a="4"
b="5"
c="6"

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

# Check if any two values are equal
if a == b or b == c or a == c:
    total = 0
else:
    total = a + b + c

print("Result:", total)
 


# 13)  Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 


a = int(input("Enter a value number: "))
b = int(input("Enter a value number: "))

if a == b or (a + b == 5) or (abs(a - b) == 5):
    print(True)
else:
    print(False)


# 14) Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20

a=int(input("enter a value"))
b=int(input("enter a value"))
sum = a + b
if 15 <= sum <= 20:
    print(20)
else:
    print(sum)

 #15) Write a Python program to calculate the length of a string. 

    string = input("Enter a string: ")
length = len(string)
print(f"The length of the string is: {length}") 

# 16) Write a Python program to count the number of characters (character frequency) in a string.

string = input("Enter a string: ")
char_count = {} 
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char, count in char_count.items():
    print(f"'{char}': {count}")
def check_numbers(a, b):
    return a == b or abs(a - b) == 5 or (a + b) == 5
# Example usage:
a = int(input("Enter first integer: "))     
b = int(input("Enter second integer: "))
print(check_numbers(a, b))  


# 17) What are negative indexes and why are they used?

# Negative indexes in Python allow you to access elements from the end of a sequence (like a list or string).
# For example, an index of -1 refers to the last element, -2 to the second last, and so on.
# They are used to simplify accessing elements without needing to know the exact length of the sequence.    
# Example:
my_list = [10, 20, 30, 40, 50]
print(my_list[-1])  # Output: 50 (last element)
print(my_list[-2])  # Output: 40 (second last element)  




# 18) Write a Python program to count occurrences of a substring in a string. 

def count_substring(string, substring):
    count = 0
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += len(substring)  # Move past the last found substring
    return count

# 19 Write a Python program to count the occurrences of each word in a given sentence.
def count_words(sentence):
    words = sentence.split()  # Split the sentence into words
    word_count = {}
    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count 

# 20) Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def swap_first_two_chars(str1, str2):
    # Swap the first two characters of each string
    if len(str1) < 2 or len(str2) < 2:
        return "Both strings must have at least two characters."
    
    new_str1 = str2[:2] + str1[2:]  # Take first two chars from str2 and rest from str1
    new_str2 = str1[:2] + str2[2:]  # Take first two chars from str1 and rest from str2
    
    return new_str1 + " " + new_str2

# 21) Write a Python program to add 'in' at the end of a given string (length 
# should be at least 3). If the given string already ends with 'ing' then 
# add 'ly' instead if the string length of the given string is less than 3, 
# leave it unchanged.

def add_suffix(word):
    if len(word) < 3:
        return word
    elif word.endswith("ing"):
        return word + "ly"
    else:
        return word + "in"

print(add_suffix("play"))    # playin
print(add_suffix("playing")) # playingly
print(add_suffix("go"))      # go
print(add_suffix("run"))     # runin

# 22)Write a Python function to reverses a string if its length is a multiple of 4.
def reverse_if_multiple_of_four(s):
    if len(s) % 4 == 0:
        return s[::-1]  # Reverse the string
    else:
        return s  # Return the original string   


# 23)2 chars from a given a string. If the string length is less than 2, return instead of the empty string.          
def first_two_chars(s):
    if len(s) < 2:
        return s  # Return the original string if length is less than 2
    else:
        return s[:2]  # Return the first two characters of the string   
    
# 24) Write a Python function to insert a string in the middle of a string.
def insert_in_middle(original, to_insert):
    mid_index = len(original) // 2
    return original[:mid_index] + to_insert + original[mid_index:]

# 25)  What is List? How will you reverse a list?


# A list in Python is a mutable, ordered collection of items that can contain elements of different data types.
# Lists are defined using square brackets [] and can be modified after creation.
# To reverse a list, you can use the built-in `reverse()` method or slicing.
def reverse_list(lst):
    return lst[::-1]  # Using slicing to reverse the list

# 26) How will you remove last object from a list?
# To remove the last object from a list in Python, you can use the `pop()` method without an index,
# which removes and returns the last item from the list. Alternatively, you can use `del


# 27) Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [1]?     

# In Python, list indexing starts at 0. Therefore, list1[1] will return the second element of the list.
# For the given list, list1[1] will return 33.

# 28) Differentiate between append () and extend () methods?
# The `append()` method adds a single element to the end of a list,
# the `extend()` method adds multiple elements from an iterable (like another list) to the end of the list.
def append_example(lst, item):
    lst.append(item)  # Adds a single item to the end of the list
    return lst



# 29) Write a Python function to get the largest number, smallest num and sum of all from a list.
def list_stats(lst):
    largest = max(lst)  # Get the largest number
    smallest = min(lst)  # Get the smallest number
    total_sum = sum(lst)  # Get the sum of all numbers
    return largest, smallest, total_sum



# 30) How will you compare two lists? 

list1 = [1, 2, 2, 3]
list2 = [3, 1, 2]

print(set(list1) == set(list2))  # True

# 31) Write a Python program to count the number of strings where the stringlength is 2 or more and the first and last character are same from a given listof strings. 
def count_matching_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count
# 32) Write a Python program to remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))  # Convert to set to remove duplicates and back to list           

# 33) Write a Python program to check a list is empty or not.
def is_list_empty(lst): 
    return len(lst) == 0  # Returns True if the list is empty, otherwise False              
# 34) Write a Python function that takes two lists and returns true if they have at least one common member
def have_common_member(list1, list2):
    return bool(set(list1) & set(list2))  # Check for intersection between two sets     
# 35 ) Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30. 
squares = [i**2 for i in range(1, 31)] 
result = squares[:5] + squares[-5:]  # First and last 5 elements
print(result)       
# 36) Write a Python function that takes a list and returns a new list withunique elements of the first list.

def unique_elements(lst):
 return list(set(lst))  # Convert to set to get unique elements and back to list


# 37) Convert a list of characters into a string

char_list = ['H', 'e', 'l', 'l', 'o']
string_result = ''.join(char_list)
print("37) String from list of characters:", string_result)


# 38) Select an item randomly from a list

import random
items = [10, 20, 30, 40, 50]
random_item = random.choice(items)
print("38) Random item from list:", random_item)


# 39) Find the second smallest number in a list

numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()
second_smallest = numbers[1]
print("39) Second smallest number:", second_smallest)


# 40) Get unique values from a list

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_values = list(set(my_list))
print("40) Unique values from list:", unique_values)


# 41) Check whether a list contains a sub list

main_list = [1, 2, 3, 4, 5]
sub_list = [3, 4]
contains = all(item in main_list for item in sub_list)
print("41) Contains sublist:", contains)


# 42) Split a list into different variables

data = [10, 20, 30]
a, b, c = data
print("42) Split list into variables:", a, b, c)


# 43) What is tuple? Difference between list and tuple

my_tuple = (1, 2, 3)
my_list2 = [1, 2, 3]

print("\n43) Tuple example:", my_tuple)
print("List example:", my_list2)

print("\nDifference between List and Tuple:")
print("1. List is mutable, Tuple is immutable")
print("2. List uses [], Tuple uses ()")
print("3. Tuples are faster and use less memory")
 
    
         