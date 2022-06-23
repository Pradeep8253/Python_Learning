alphabet = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' ,
            'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z','a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' ,
            'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']

def caeser(start_text , shift_amount , cipher_direction):
    end_text= ""
    if cipher_direction == "decode":
        shift_amount*=-1
    for char in start_text:
        if char in alphabet :
           position = alphabet.index(char)
           new_position = position + shift_amount
           end_text += alphabet[new_position]
        else:
           end_text+= char
           # TODO 3 : WHAT HAPPEND when user enters a number/symbol/space ?
           # can you fix the code to keep the number / symbol / space when the text is encoded or decoded ?
           # e.g. start_text = "meet me at 3"
           # end_text = ".... .. .. 3 "
    print(f"here's the {cipher_direction} result : {end_text}")

  # TODO 1 - print the cipher text massage
#print("welcome to the cipher caeser text !\n")
  # TODO 4 - can you figure out a way to ask the user if they want to restart the cipher program?
  # e.g. type 'yes' if you want to go again , otherwise you type 'no'.
 # if they type 'yes' then ask them for the direction /shift/ shift again and call  the ceaser {} function again?

 # H
# INT - try creating new that calls itself if they type 'yes'.

should_continue = True
while should_continue :
    direction = input("type 'encode' to encrypt , type 'decode' to decrypt : \n ")
    text = input ("type your massage : \n") . lower()
    shift = int(input("type the shift number: \n"))

 # TODO - 2:- what if the user enters a shift that is greater than the number of letters in the alphabets?
 # try running the program and entering a shift number of 45
 # HINT - think about how you can use the modulus (%) .
shift = shift % 26
caeser(start_text=text , shift_amount=shift , cipher_direction=direction)

result = input(" type 'yes' if you want to go again . otherwise type 'no' .\n")
if result == "no":
  should_continue= False
print("good bye .")