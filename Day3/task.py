                #Can you Ride the RollerCoaster
                 
# If Else condition check
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# Nested if Statements & elif statements
if height >= 120:
    print("You can ride the rollercoaster") 
    age = int(input("What is your age? "))
    if age <= 12: 
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    photos = input("Would you like to have a photo taken for $3? y for yes, n for no. ")
    if photos == "y":
        bill += 3
        
    print(f"Your Total is ${bill}, Enjoy the ride!")
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
    
    
            # BMI Calculator with Interpretations

weight = int(input("Please enter your Weight in kilos: "))
height = float(input("Please enter you height in meters: "))

bmi = weight / height ** 2 

if bmi <= 18.5:
    print("Acording to science you are under weight!")
elif bmi <= 25:
    print("Congrats you weight is normal.. (according to science)")
else:
    print("According to scienctific research algorithms you are overweight, sorry!")