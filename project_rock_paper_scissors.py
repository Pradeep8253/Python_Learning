# don't change the code below
student_heights= input(" inputs a list of the student heights .").split()
for n in range (0 , len(student_heights)):
     student_heights[n] = int(student_heights[n])
print(student_heights)

# don't change the above code


#write the code  below this line
# total_height = sum(student_heights)
total_height= 0
for height in  student_heights:
    total_height += height
    print(total_height)

number_of_student = 0
for student in student_heights:
    number_of_student +=1
    print(number_of_student)

number_of_student = len(student_heights)
average_height = round(total_height/number_of_student)
print(average_height)

