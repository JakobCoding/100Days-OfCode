# For Loops
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits: 
    print(fruit)
    
# How to Add up numbers in a list

student_scores = [150, 200, 199, 126, 186, 99, 55, 66, 88, 139]
total_exam_scores = sum(student_scores)
print(total_exam_scores) # console = 1308

# How to use a for loop to create a sum from a list

sum = 0
for score in student_scores:
    sum += score
    
print(sum) # console = 1308