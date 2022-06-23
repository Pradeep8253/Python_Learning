print("welcome to the tip calculator ! ")

bill = float(input("what are the total bill? "))

tip = int(input(" what percentage of tip would you like to give ? 10 , 12 , or 15  ?"))
people = int(input(" how many people to spilt the bill ? "))

tip_amount = tip / 100 * bill
total_bill = bill + tip_amount

bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"each person should pay : ${final_amount} ")
