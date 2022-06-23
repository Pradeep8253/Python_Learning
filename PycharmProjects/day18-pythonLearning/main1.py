import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


# colors = ["red", "light blue", "lime", "gold", "light slate blue", "purple", "olive drab", "orange",
#         "dark cyan"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# def draw_shape(num_sides):
#     angle = 365 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors)
#     draw_shape(shape_side_n)

tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
