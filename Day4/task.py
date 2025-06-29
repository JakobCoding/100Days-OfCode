# Randomisation - import random module
import random

# randomInt = random.randint(1, 100)
# print(randomInt)

# print(myModule.myFavoriteNumber)

# Generating Floating point number in the range of 0.0 - < 1
# randomNumber0_1 = random.random() * 10 # extend range past 1
# print(randomNumber0_1)

# # Generate Floating point numbers in a aspecified range
# randomFloat = random.uniform(1, 100)
# print(randomFloat)

# Random Head or Tails

# headsOrTails = random.randint(0, 1)
# if headsOrTails == 0:
#     print("Heads")
# else:
#     print("Tails")
    
# Lists - always start within square brackets seperated by a commer

statesOfAmerica = ["Deleware", "California", "NewYork"]
print(statesOfAmerica[-1])

# Add item to end of the list 
statesOfAmerica.append("JakeState")
print(statesOfAmerica[-1])

# print random name from list of friends
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# 1st option
print(random.choice(friends))

# 2nd option
randomIndex = random.randint(0, 4)
print(friends[randomIndex])