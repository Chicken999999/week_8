#zip (*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.) It creates a zip object with paired elements store in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")

users = zip(usernames, passwords)


for i in users:
    print(i)

student_names = ["Steven", "Jackie", "Donna", "Kelso"]
student_ids = [1000, 2333, 33445, 45556]
student_ages = [22, 34, 45, 56]
student_gpas = [3.0, 4.0, 3.5, 3.7]
zipped_items = zip(student_names, student_ids, student_gpas)

for i in zipped_items:
    print(i)
######################################### zip in python############################################



# Zip Practice #1
# Print to the screen phrases like the following example:

# "The capital of Germany is Berlin"

# Use the zip function, loops, and the following lists of countries and capitals to solve it quickly and efficiently.

# capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
# countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]



# Zip Practice #2
# Create a zip object made up of lists, of a set of brands and products that you prefer, inside the my_zip variable.
# brands =
# products =


# Zip Practice #3
# Create a zip object with the translations of the numbers from 1 to 5 in Spanish, Portuguese and English (in that same order), and then convert the generated object into a list called numbers:

# one / um / one

# two / two / two

# three / three / three

# four / four / four

# five / five / five

# The result should follow the structure:

# [('one', 'um', 'one'), ('two', 'dois', 'two'), ... ]

# 1: uno / um / one
# 2: dos / dois / two
# 3: tres / três / three
# 4: cuatro / quatro / four
# 5: cinco / cinco / five


#######################zip function challenge#####################
# Challenge: Create a list of countries and their capitals, then zip them together and print
# each country with its capital.

# Two lists: countries and capitals


# Use zip to pair countries with their capitals