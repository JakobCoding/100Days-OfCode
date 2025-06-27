# Subscripting - Prints the letter at 0 index
# prints first letter
print("Hello"[0])

# prints last letter 
print("Hello"[-1])

# Integer = Whole number
print(123 + 456)

# Floats - decimal point numbers (floating point number)
print(3.14159)

# Boolean - True or False values only 
print(type(True))
print(False)

# converting data types 
print(len(str(12345)))

# checking data types / type checking 
print(type("Hello"))
print(type(True))
print(type(1234))
print(type(3.14))

# Type Conversion / Type Casting 
print(int("123") + int("435"))

# Debug challange
print("Number of letters in your name: " + (str(len(input("Enter your name ")))))

# debug Challange 2.0 / type conversion 
name_of_user = input("What is your name? \n")
length_of_name = len(name_of_user)

print(type(name_of_user)) # string
print(type(length_of_name)) # int

print("Number of letters in your name: " + str(length_of_name))

# Mathematical Operations 
print("My age: " + str(39))
print(5 / 3) # basic divison provides a floating point number
print( 5 // 3) # Double division lines produce a whole number (interger)
print(2 ** 3) # exponents represents 2 to the power of 3 

# PEMDASLR - The order of mathematical operations 
# Parentheses , Exponenets , Multiplication , Addition , Subtraction & Left to Right
#  ()
#  **
#  * OR /
#  + OR -

# when things of equal importance it goes from left to right 
print(3 * 3 + 3 / 3 - 3) # = 7

# (3 * 3 = 9) + (3 / 3 = 1) - 3 therefore 9 + 1 - 3 = 7

# Change the code to equal 3 
print(3 / 3 * 3 + 3 - 3) # = 3
print(3 * (3 + 3) / 3 - 3) # = 3