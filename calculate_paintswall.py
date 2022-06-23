# write the code below these line
import math


def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"you'll need {num_of_cans} cons of paint.")


# write the code above these line

# don't change the code below
test_h = int(input("height of the wall : "))
test_w = int(input("width of  wall : "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
