# If Else condition check
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster") 
else: 
    print("Sorry you have to grow taller before you can ride.")    
    
# Modulo Operator % is a binary operator and provides the remainder between 2 numbers
print(10 % 5) # modulo = 0 
print(10 % 3) # modulo = 1

# Write some code that checks if a number is odd or even 

num1 = int(input("Enter a number: "))
 

if num1 % 2 == 0: 
    print("Even Number!")
else:
    print("Odd number!")