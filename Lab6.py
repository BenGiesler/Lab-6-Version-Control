# Ben Giesler
#Funtions that prints the menu
def print_menu():
    print("Menu \n"
          "------------- \n"
          "1. Encode \n"
          "2. Decode \n"
          "3. Quit \n")

#encoding function
def encode(passwords):
    global encoded_password
    #Goes through each number and adds 3, while accounting for numbers above 6
    for letter in passwords:
        encoded_password += str(((int(letter) + 3) % 10))
    print("Your password has been encoded and stored! ")

#decoding function
def decode(enc_pass):
    pass

if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            encoded_password = ''
            password = input("Please enter your password: ")
            encode(password)
        elif choice == "2":
            decode(encoded_password)
        elif choice == "3":
            break


