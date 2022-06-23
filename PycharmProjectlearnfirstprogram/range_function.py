# for loop with range
'''total = 0
for number in range (1 , 101  ):
    total+=number
print(total)'''

# adding even exercise
'''
total = 0
for number in range (1 , 101 , 2 ):
    total+=number
print(total)

total2 = 0
for number in range (1 , 101 ):
    if number%2 ==0 :
        total2+=number
print(total2) '''

for number in range (1 , 101):
    if number%3 == 0 and number %5 == 0 :
        print("FizzBuzz")
    elif number%3 == 0 :
        print("fizz")
    elif number%5 == 0 :
        print("Buzz")
    else:
        print(number)
