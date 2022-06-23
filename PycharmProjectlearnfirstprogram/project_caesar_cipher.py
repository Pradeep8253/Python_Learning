alphabet = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' ,
            'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z','a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' ,
            'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']


direction = input(" type 'encode' to encrypt , type 'decode' to decrypt : \n")
text = input("type your massage : \n").lower()
shift = int(input("type the shift number : \n"))

print("WELCOME TO THE CAESAR CIPHER ! ")

def caesar(start_text  , shift_amount , cipher_direction):
    end_text=""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction=="encode":
            new_position = position +shift_amount
        elif cipher_direction=="decode":
            new_position=position-shift_amount
            end_text+=alphabet[new_position]
    print(f"the {cipher_direction} text is {end_text}")

caesar(start_text=text , shift_amount=shift , cipher_direction=direction)

# don't change the code above

#TODO-1 : create a function called 'encrypt' that takes the 'text' and 'shift' inputs .

  # TODO-2 : inside the 'encrypt' function , shift each letter of the 'text forwords in the alphabet vy the shift amount
  # and print the encrypted text.

  # e.g.
  # plain_text = "hello"
  # shift = 5
  # cipher_text = "mjqqt"
  # print output : " the encoded text is mjqqt "

def encrypt(plain_text , shift_amount):
   cipher_text=""
   for letter in plain_text:
      position= alphabet. index(letter)
      new_position= position+shift_amount
      new_letter = alphabet[new_position]
      cipher_text+=new_letter
   print(f"the encoded text is {cipher_text}")

#TODO-3: call the encrypt function and pass in the user inputs . you should be able to test the code
#       and encrypt the massage
#encrypt(plain_text=text , shift_amount=shift)

#FOR DECRYPT

def decrypt(cipher_text , shift_amount):
    plain_text = ""
    for letter in cipher_text:
      position= alphabet . index(letter)
      new_position= position-shift_amount
      plain_text +=  alphabet[new_position]
    print(f"the decoded text is {plain_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text , shift_amount=shift)

