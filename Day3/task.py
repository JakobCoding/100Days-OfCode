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
    
                
                    # PYTHON PIZZA SERVICE #

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extraCheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Sorry please enter S, M or L pizza size.")
    
# todo: work out how much to add to their bill based on their pepporoni choice    
    
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
    
# todo: work out their final amount based on whether if they want extra cheese 

if extraCheese == "Y":
    bill += 1


print(f"Your final bill is: ${bill}, enjoy!") 

#Logical Operators

# and 
# or 
# not

#  A and B have to be true for the entire line of code to be true 
#  C or D has to be true for the entire line of code to be true
#  not E 