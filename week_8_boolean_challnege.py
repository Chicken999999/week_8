#######################boolean expressions challenges#####################
# 20 points each challenge...
# problem 1: Check if a number is both even and divisible by 5.
# The program prompts the user for a number, checks whether it meets both conditions 
# (even and divisible by 5), and then outputs the result to the console.
# num = int(input("Enter a number: "))
# divisible = num % 5 == 0 

# ask = int(input("Enter a number: "))
# even = ask % 2 == 0

# print(divisible and even)
# Prompt the user for a number

# Check if the number is even and divisible by 5

# Output the result to the console


# Problem 2: Number in Range
# Description:
# Create a program that checks whether a given number falls within a specified range, such as 10 to 20 (inclusive).

# Input: A number (integer)
# Output: "The number is within the range." or "The number is outside the range."
# Hint:
# Use the and operator to check if the number is greater than or equal to 10 and less than or equal to 20.

# integer = 12



# Problem 3: Password Strength Checker
# Description:
# Write a program that checks if a user's password meets the following criteria:

# At least 8 characters long

# Contains at least one digit (0-9)

# Input: Password (string)

# Output: "Password is strong." or "Password is weak."

# Hint:
# Use the len() function to check the length and the any() function with a generator expression to check for a digit.
# password = input("Type your password: ")
# length = len(tuple(password)) > 7
# # this function checks if any character in the password string is a number, if so it returns true
# digit_checker = [char.isdigit() for char in password]
# print(length)
# print(any(digit_checker)) 


# Problem 4: Odd or Even and Multiple of 3
# Description:
# Create a program that determines if a number is odd or even and also checks if it is a multiple of 3.

# Input: A number (integer)
# Output:
# "Even and a multiple of 3."
# "Even but not a multiple of 3."
# "Odd and a multiple of 3."
# "Odd but not a multiple of 3."
# Hint:
# Use % for both the even check and the multiple of 3 check.
num = int(input("Input a number: "))
even_or_false = num % 2 == 0
multiple_of_three = num % 3 == 0 
if even_or_false and multiple_of_three :
    print("Even and a multiple of 3")
elif even_or_false and not multiple_of_three:
    print("Even but not a multiple of 3.")
elif not even_or_false and multiple_of_three:
    print("Odd and a multiple of 3.")
elif not even_or_false and not multiple_of_three:
    print("Odd but not a multiple of 3.")


# Problem 5: Vowel or Consonant
# Description:
# Write a program that takes a single character as input and checks whether it is a vowel or a consonant. Assume the input is a lowercase letter.

# Input: A character (string of length 1)
# Output: "Vowel" or "Consonant"
# Hint:
# Use the in operator to check if the character belongs to the set {'a', 'e', 'i', 'o', 'u'}.