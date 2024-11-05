alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# USE: start the program write 'encode' then type whatever you wish to encode. 'Shift' how much of a shift you want on the ceaser cipher.
# After type 'yes' to continue then 'decode' copy what was outputed on the encode then paste on the input line and the amount of shift you asked for.
# Then whatever you encrypted should be there in its original form.

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")


# While loop to see if the user wants to continue the ceaser cipher
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  # Makes all inputs lowercase
  text = input("Type your message:\n").lower()
  # Asks the user for number of shifts for the cipher
  shift = int(input("Type the shift number:\n"))
  # Shifts the letters more to create different combos of letters depending on user shift
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
# Restars at the 'encode', 'decode' message if typed 'yes' and exits if type 'no'
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")