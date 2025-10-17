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

#  4) Write a Python program to check if a number is positive, negative or zero.??


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
my_list = [1, 2, 3]
a, b, c = my_list
print("42) Split list into variables:", a, b, c)    


# 43) What is tuple? Difference between list and tuple.

# Tuple: A tuple in Python is an ordered, immutable collection of elements.
# Tuples are defined using parentheses () and can store elements of different data types.

# Difference between List and Tuple:
# 1. List is mutable (can be changed), Tuple is immutable (cannot be changed).
# 2. List uses [], Tuple uses ().
# 3. Lists have more methods; Tuples have fewer methods.
# 4. Tuples are faster and use less memory compared to lists.

# Example to show mutability
my_list = [1, 2, 3]
my_list[0] = 10  # Allowed
print("Modified List:", my_list)

my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # ❌ Not allowed (immutable)
print("Tuple:", my_tuple)


# 44) Python program to create a tuple with different data types
mixed_tuple = (25, "Python", 3.14, True)
print("\nTuple with different data types:", mixed_tuple)


# 45) Python program to unzip a list of tuples into individual lists
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, chars = zip(*list_of_tuples)  # Unzipping
print("\nNumbers list:", list(nums))
print("Characters list:", list(chars))


# 46) Python program to convert a list of tuples into a dictionary
list_of_tuples_dict = [('name', 'John'), ('age', 25), ('city', 'New York')]
my_dict = dict(list_of_tuples_dict)
print("\nDictionary from list of tuples:", my_dict)


# 47) Create a dictionary using tuples in Python

# Keys and values can be tuples
dict_with_tuples = {('name', 'first'): 'John', ('age', 'years'): 25}
print("\nDictionary with tuple keys:", dict_with_tuples)

# Using tuple of pairs
tuple_pairs = (('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964))
dict_from_tuples = dict(tuple_pairs)
print("Dictionary from tuple of pairs:", dict_from_tuples)


# 48) Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {'a': 10, 'b': 5, 'c': 30, 'd': 20}

asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

print(" Sorted Ascending:", asc)
print(" Sorted Descending:", desc)


# 49) Write a Python script to concatenate following dictionaries to create a new one.
dict1 = {1: "A", 2: "B"}
dict2 = {3: "C", 4: "D"}
dict3 = {5: "E", 6: "F"}

new_dict = {}
for d in (dict1, dict2, dict3):
    new_dict.update(d)

print("Concatenated Dictionary:", new_dict)


# 50) Write a Python script to check if a given key already exists in a dictionary.
my_dict2 = {'name': 'Aryan', 'age': 21, 'city': 'Pune'}
key = 'age'

if key in my_dict2:
    print(f" Key '{key}' exists in dictionary.")
else:
    print(f" Key '{key}' does not exist.")


# 51) How Do You Traverse Through a Dictionary Object in Python?
print(" Traversing dictionary:")
for k, v in my_dict2.items():
    print(f"  Key: {k}, Value: {v}")


# 52) How Do You Check the Presence of a Key in A Dictionary?
if 'city' in my_dict2:
    print(" Key 'city' is present.")
else:
    print(" Key 'city' is not present.")


# 53) Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
dict_1_15 = {x: x**2 for x in range(1, 16)}
print(" Dictionary 1 to 15:", dict_1_15)

# 55) Write a Python script to merge two Python dictionaries.
dict1 = {'a': 100, 'b': 200}
dict2 = {'c': 300, 'd': 400}

# Method 1: Using update()
merged_dict = dict1.copy()
merged_dict.update(dict2)

print("Merged Dictionary:", merged_dict)

# Method 2: (Python 3.9+) Using |
# merged_dict = dict1 | dict2
# print("Merged Dictionary:", merged_dict)


# 56) Write a Python program to map two lists into a dictionary.
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

from collections import Counter

keys = ['a', 'b', 'c', 'd']
values = [400, 400, 300, 400]

mapped_dict = dict(zip(keys, values))
counter_dict = Counter(mapped_dict)

print("Mapped Dictionary with Counter:", counter_dict)

# 57) Write a Python program to find the highest 3 values in a dictionary.
my_dict = {'a': 100, 'b': 400, 'c': 300, 'd': 200, 'e': 500}

top3 = sorted(my_dict.values(), reverse=True)[:3]
print("Highest 3 values:", top3)


# 58) Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

from collections import Counter

data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

counter = Counter()
for d in data:
    counter[d['item']] += d['amount']

print("Combined values:", counter)


# 59) Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.

string = "programming"
letter_count = {}

for char in string:
    letter_count[char] = letter_count.get(char, 0) + 1

print("Dictionary from string:", letter_count)


# 57) Write a Python program to find the highest 3 values in a dictionary.
my_dict = {'a': 100, 'b': 400, 'c': 300, 'd': 200, 'e': 500}

top3 = sorted(my_dict.values(), reverse=True)[:3]
print("Highest 3 values:", top3)


# 58) Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

from collections import Counter

data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

counter = Counter()
for d in data:
    counter[d['item']] += d['amount']

print("Combined values:", counter)


# 59) Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.

string = "programming"
letter_count = {}

for char in string:
    letter_count[char] = letter_count.get(char, 0) + 1

print("Dictionary from string:", letter_count)


# 60) Sample string: 'w3resource'
# Expected output: {'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

sample = "w3resource"
count_dict = {}

for char in sample:
    count_dict[char] = count_dict.get(char, 0) + 1

print("Letter count from 'w3resource':", count_dict)


# 61) Write a Python function to calculate the factorial of a number (a nonnegative integer).
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# 62) Write a Python function to check whether a number is in a given range.
def in_range(num, start, end):
    return start <= num <= end

print("Is 7 in range 5–10?:", in_range(7, 5, 10))
print("Is 15 in range 5–10?:", in_range(15, 5, 10))


# 63) Write a Python function to check whether a number is perfect or not.

# Perfect number: sum of divisors (excluding itself) == number
def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

print("Is 28 a perfect number?:", is_perfect(28))
print("Is 12 a perfect number?:", is_perfect(12))

# 64) Write a Python function that checks whether a passed string is palindrome or not.
def is_palindrome(s):
    return s == s[::-1]

print("Is 'madam' a palindrome?:", is_palindrome("madam"))
print("Is 'python' a palindrome?:", is_palindrome("python"))


# 65) How Many Basic Types of Functions Are Available in Python?
# There are 2 basic types of functions in Python:
# 1. Built-in Functions (e.g., len(), print(), type(), sum(), etc.)
# 2. User-defined Functions (functions created by the programmer)


# 66) How can you pick a random item from a list or tuple?
import random

items_list = [10, 20, 30, 40, 50]
items_tuple = ('a', 'b', 'c', 'd')

print("Random item from list:", random.choice(items_list))
print("Random item from tuple:", random.choice(items_tuple))


# 67) How can you pick a random item from a range?
print("Random item from range 1–10:", random.choice(range(1, 11)))


# 68) How can you get a random number in Python?
print("Random number between 1 and 100:", random.randint(1, 100))


# 69) How will you set the starting


random.seed(10)  # Setting seed ensures same sequence every time
print("Random number after setting seed:", random.randint(1, 100))

# 70) How will you randomize the items of a list in place?
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Randomized list:", numbers)


# 71) What is File function in python? What are keywords to create and write file.

# In Python, the built-in function open() is used for file handling.
# Modes:
# "r" – read, "w" – write, "a" – append, "x" – create
# "t" – text (default), "b" – binary
# Example:
file = open("sample.txt", "w")
file.write("Hello, this is a test file.")
file.close()


# 72) Write a Python program to read an entire text file.
with open("sample.txt", "r") as f:
    content = f.read()
print("Entire file content:\n", content)


# 73) Write a Python program to append text to a file and display the text.
with open("sample.txt", "a") as f:
    f.write("\nAppending new line.")
with open("sample.txt", "r") as f:
    print("File after append:\n", f.read())


# 74) Write a Python program to read first n lines of a file.
n = 2
with open("sample.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")


# 75) Write a Python program to read last n lines of a file.
n = 2
with open("sample.txt", "r") as f:
    lines = f.readlines()
print("Last n lines:", "".join(lines[-n:]))


# 76) Write a Python program to read a file line by line and store it into a list.
with open("sample.txt", "r") as f:
    lines_list = f.readlines()
print("File as list:",lines_list)
# 77) Write a Python program to read a file line by line store it into a variable.
with open("sample.txt", "r") as f:
    file_content = "".join(f.readlines())
print("File stored into variable:\n", file_content)


# 78) Write a python program to find the longest words.
with open("sample.txt", "r") as f:
    words = f.read().split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)


# 79) Write a Python program to count the number of lines in a text file.
with open("sample.txt", "r") as f:
    line_count = sum(1 for line in f)
print("Number of lines:", line_count)


# 80) Write a Python program to count the frequency of words in a file.
from collections import Counter
with open("sample.txt", "r") as f:
    words = f.read().split()
word_freq = Counter(words)
print("Word frequency:", word_freq)


# 81) Write a Python program to write a list to a file.
my_list = ["Python", "Java", "C++", "C"]
with open("listfile.txt", "w") as f:
    for item in my_list:
        f.write(item + "\n")
print("List written to file successfully.")


# 82) Write a Python program to copy the contents of a file to another file.
with open("sample.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())
print("File copied successfully.")


# 83) Explain Exception handling? What is an Error in Python?

try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Error occurred:", e)


# 84) How many except statements can a try-except block have? Name Some built-in exception classes:

# A try block can have multiple except clauses.
# Common built-in exceptions: ZeroDivisionError, ValueError, TypeError, KeyError, FileNotFoundError


# 85) When will the else part of try-except-else be executed?
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("That's not a valid number!")
else:
    print("No error occurred, so else block executed.")



# 86) Can one block of except statements handle multiple exception?

# Yes, by using a tuple of exceptions.
try:
    val = int("abc")
except (ValueError, TypeError) as e:
    print("Handled multiple exceptions:", e)


# 87) When is the finally block executed?

# The finally block is always executed whether an exception occurs or not.
try:
    x = 10 / 2
finally:
    print("Finally block executed.")


# 88) What happens when "1" == 1 is executed?

# It returns False because one is a string and the other is an integer.
print('"1" == 1 →', "1" == 1)


# 89) How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding snippets.
try:
    num = int("xyz")
except ValueError:
    print("Handled ValueError.")
finally:
    print("Finally block always runs.")


# 90) Write python program that user to enter only odd numbers, else will raise an exception.
try:
    num = int(input("Enter an odd number: "))
    if num % 2 == 0:
        raise ValueError("That is not an odd number!")
    print("You entered an odd number:", num)
except ValueError as e:
    print("Error:", e)

#end of module 7 - :)