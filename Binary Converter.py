while True:
    # Greeting the user and asking what number they want to convert
    user_input = input("Hello! What number do you want to convert today?\n")

    # This will attempt to save their input as an integer.  If it cannot, it'll ask them to re-enter an actual number
    while True:
        try:
            number = int(user_input)
            break
        except ValueError:
            user_input = input("That isn't a number. Please input a number:\n")
    
    # If we determine its a real number, we continue
    print("Alright! Give me one moment.")

    # Now we can calculate the conversion
    # " // " = floor divison and or integer divison, it'll keep dividing the remainder by 2 down to the lowest whole number
    binary = " "
    while True:
        if number > 0:
            remainder = number % 2
        binary = str(remainder) + binary
        number //= 2 
        
        # Now we can print the conversion
        if number == 0:
            print("---------------------")
            print(f"{user_input} in binary is {binary}")
            print("---------------------")
            break

    # Here we ask if the user would like to convert another number
    keep_going = input("Would you like to convert another number?\n")
    if keep_going.lower() == "no":
        print("Goodbye!")
        break
    if keep_going.lower() == "yes":
        continue
    else:
        print("Invalid input. Will assume no. Have a good day!")
        break