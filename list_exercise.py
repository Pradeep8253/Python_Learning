# split string method

import random
names_string = input("give me everybody's name , separated by a comma .")
names = names_string.split(" , ")

num_items = len(names)

random_choice = random.randint(0 , num_items-1)
person_who_will_play = names[random_choice]

print(person_who_will_play+" is going to buy the meal today")
