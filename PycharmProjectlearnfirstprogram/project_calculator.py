# CALCULATOR
logo=logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# add
def add(n1 , n2 ):
    return n1+n2

#substract
def substract(n1, n2):
    return n1-n2

# multiply
def multiply(n1 , n2):
    return n1*n2

# divide
def divide(n1 , n2):
    return n1/n2
operations ={
    "+":add,
     "-":substract,

    "*": multiply ,
    "/":divide
}
def calculator() :
    print(logo)
    num1=float(input("what's the  first number ? : "))
    for symbol in operations:
        print(symbol)
    should_continue=True

    while should_continue:
      operations_symbol = input("pick an another operation  : ")
      num2 = float(input("what's the second number ? :"))

      calculation_function = operations[operations_symbol]
      answer = calculation_function(num1 , num2)

      print(f"{num1} {operations_symbol}{num2} = {answer}")
    #if input(f"type 'y' to continue calculating with {answer} , or type 'n' to  exit:") =="y":
      if input(f"type 'y' to continue calculating with {answer} , or type 'n' to  start a new calculation ") =="y":
          num1= answer
      else:
          should_continue=False
          calculator()
calculator()

# WE USE ANOTHER WAY

# operations_symbol=input("pick another operation :")
# num3=int(input("what is the next number ? "))
# calculation_function=operations[operations_symbol]
# second_answer=calculation_function(first_answer , num3)
# # second_answer=operations(first_answer = calculation_function(num1 , num2), num3)

# print(f"{first_answer} {operations_symbol} {num3} = {second_answer}")
