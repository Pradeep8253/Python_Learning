# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
#
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
#
# except KeyError as error_massage:
#     print(f" the key {error_massage} does not exit")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     raise TypeError("the error is found ")

height = float(input("height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError("human height should not be over 3 meters. ")

bmi = weight / height ** 2

print(bmi)
