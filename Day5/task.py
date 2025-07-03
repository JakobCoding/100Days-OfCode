# # For Loops
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits: 
#     print(fruit)
    
# # How to Add up numbers in a list using sum() function

# student_scores = [150, 199, 126, 186, 99, 55, 66, 88, 139, 200]
# total_exam_scores = sum(student_scores)
# print(total_exam_scores) # console = 1308

# # How to use a for loop to create a sum from list items

# sum = 0
# for score in student_scores:
#     sum += score
    
# print(sum) # console = 1308

# # Use Max function to print the max value in a list

# print(max(student_scores)) # console = 200 

# # finding Max value in a list using a for loop

# max_score = 0 # Initialise max_score to 0 
# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print(max_score) # console = 200 

# Using Range with a for loop
for number in range(1, 11, 3):
    print(number)

# Add up all the numbers from 1 to 100 using a for loop
total = 0 
for number in range(1, 101):
    total += number
    print(total)
    
print(total)
