# Password Generator Project
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("how many numbers would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))


 
# EASY LEVEL #
# Initialise Password to empty string
password = ""
# Use for loop to to pick from a range of characters from letters list 
for char in range (1, num_letters + 1): 
    random_char = random.choice(letters)
    password += random_char
    
# print(password)
	

# Use for loop to to pick from a range of characters from letters list 
for num in range (1, num_numbers + 1): 
    random_num = random.choice(numbers)
    password += random_num
    
# print(password)


# Use for loop to to pick from a range of characters from letters list 
for sym in range (1, num_symbols + 1): 
    random_symbol = random.choice(symbols)
    password += random_symbol
    
print(password)
