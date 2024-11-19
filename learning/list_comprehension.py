

# list_comprehension = A concice way to create lists in ppython; 
#                     compact and easier to read than traditional loops; 
#                     [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)

# print(doubles)


# doubles = [x * 2 for x in range(1, 11)]
# print(doubles)

# triples = [y * 3 for y in range(1, 11)]
# print(triples)

# squares = [z ** 2 for z in range(1, 11)]
# print(squares)

# fruits = ["apple", "orange", "banana", "coconut"]

# fruits = [fruit.upper() for fruit in fruits] # makes all the letters upper case 
# print(fruits)

# fruit_chars = [fruit[0] for fruit in fruits] # takes the first letter of rach fruit into a new list 
# print(fruit_chars)

# numbers = [1, -2, 3, -4, 5, -6, 8, -7]

# positive_nums = [num for num in numbers if num >= 0] #returns all positive values
# print(positive_nums)

# negative_nums = [num for num in numbers if num < 0]
# print(negative_nums)

# even_nums = [num for num in numbers if num % 2 == 0]
# print(even_nums)

# odd_nums = [num for num in numbers if num % 2 == 1]
# print(odd_nums)

# grades = [85, 42, 79, 90, 56, 61, 30]

# passing_grades = [grade for grade in grades if grade >= 60] # only all values greater than 60 
# print(passing_grades)


# # 1.
# numbers = [3, 7, 10, 15, 21]
# doubled_values = [num * 2 for num in numbers]
# print(doubled_values)

# # 2.
# values = [8, 11, 20, 25, 32, 47, 55]
# odd_numbers = [num for num in values if num % 2 == 1]
# print(odd_numbers)

# # 3. 
# words = ["apples", "banana", "cherry", "date"]
# word_lengths = [len(word) for word in words]
# print(word_lengths)

# # 4. 
# nums = [4, 5, 6, 7, 8, 9, 10]
# squared_evens = [num ** 2 for num in nums if num % 2 == 0]
# print(squared_evens)

# # 5. 
# names = ["Alice", "Bob", "Amanda", "Charlie", "Anna", "Charlie"]
# names_starting_with_a = [name for name in names if name[0] == "A"]
# print(names_starting_with_a)
# # 6. 
# sentence = ["hello", "world", "python", "is", "great"]
# uppercase_words = [word.upper() for word in sentence]
# print(uppercase_words)

################################################List comprehension###############################################
# List Comprehensions Practice #1
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create a square_values list consisting of the numbers in the values list, squared.

values = [1, 2, 3, 4, 5, 6, 9.5]

values_squared = [num ** 2 for num in values]

print(values_squared)

# List Comprehensions Practice #2
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create an even_values list consisting of the numbers in the values list that (you guessed it!) are even.

values = [1, 2, 3, 4, 5, 6, 9.5]

even_values = [num for num in values if num % 2 == 0]

print(even_values)

# List Comprehensions Practice #3
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# For the following list of temperatures in degrees Fahrenheit, express these same values in a new list of temperature values in degrees Celsius. The conversion between type of units is as follows:

# °C = (°F - 32) * (5/9)

# or expressed in another way:

# (degrees_fahrenheit-32)*(5/9)

# The list of temperatures is as follows:

# temperature_fahrenheit = [32, 212, 275]

# Store this new list in a variable called degrees_celsius




