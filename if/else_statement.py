print("welcome to rollercoaster !")
height=int(input("what is your height in cm ?"))

if height>=120 :
    print("you can ride the rollercoaster !")
    age = int(input("what is your age ? "))
    if age<12:
        print("please pay $5.0")
    elif age <= 18:
        print("please pay $7.0")
    else:
        print("please pay $12.0 ")
else :
    print("sorry , you have to grow taller before you can ride .")