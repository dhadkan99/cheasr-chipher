import string

alphabets = string.ascii_uppercase  # imports alphabets in uppercase

def welcome():
    print("Welcome to Caesar Cipher\nThis program encrypts and decrypts texts using Caesar Cipher.")

def write_output(message, output_filename):
    with open(output_filename, "w") as output_file:
        output_file.write(message)
    print(f"Output written to {output_filename}")

def encrypt(plaintext, key, output_filename="results.txt"):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.upper()
        if letter == " ":
            ciphertext += letter  # handle spaces
        if not letter == " ":
            index = alphabets.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = (index + key) % 26  # handle rotation
                ciphertext += alphabets[new_index]

    print(ciphertext)  # print the encrypted message
    write_output(ciphertext, output_filename)
    continue_program()

def decrypt(ciphertext, key, output_filename="results.txt"):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.upper()
        if letter == " ":
            plaintext += letter  # handle space
        if not letter == " ":
            index = alphabets.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = (index - key) % 26  # handle rotation
                plaintext += alphabets[new_index]

    print(plaintext)  # decrypt output
    write_output(plaintext, output_filename)
    continue_program()

def continue_program():
    again = input("Do you want to encrypt or decrypt again? (y/n): ")
    if again.lower() == "y":
        combine()
    elif again.lower() == "n":
        thanks()

def enter_message():
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode == "e" or mode == "d":
            break
        else:
            print("Invalid Mode")

    if mode == "e":
     
        user_input = input("Would you like to read from a file (f) or the console (c)?: ")
        if user_input.lower() == 'f':
            while True:
                filename = input("Enter a filename: ")
                try:
                    with open(filename, "r") as file:
                        text = file.read()
                    break
                except FileNotFoundError:
                    print(f"Invalid Filename.")
        elif user_input.lower() == 'c':
            text = input("What message would you like to encrypt: ")
        else:
            print("Invalid choice for reading source (f/c)")
            

        shift_number = input("What is the shift number: ")
        if shift_number.isdigit():
            shift_number = int(shift_number)
        else:
            print("Invalid Shift")
            

        output_filename = input("Output Written to : ") or "results.txt"  # press Enter for default 'results.txt'
        encrypt(text, shift_number, output_filename)

    elif mode == "d":
        
        user_input = input("Would you like to read from a file (f) or the console (c)?: ")
        if user_input.lower() == 'f':
            while True:
                filename = input("Enter a filename: ")
                try:
                    with open(filename, "r") as file:
                        text = file.read()
                    break
                except FileNotFoundError:
                    print(f"Invalid Filename.")
        elif user_input.lower() == 'c':
            text = input("What message would you like to decrypt: ")
        else:
            print("Invalid choice for reading source (f/c)")
            

        shift_number = input("What is the shift number: ")
        if shift_number.isdigit():
            shift_number = int(shift_number)
        else:
            print("Invalid Shift")
            

        output_filename = input("Output Written to: ") or "results.txt"  # press Enter for default 'results.txt'
        decrypt(text, shift_number, output_filename)

def thanks():
    print("Thanks for using the program, Goodbye!!")  # goodbye message

def combine():
    welcome()
    enter_message()

combine()
