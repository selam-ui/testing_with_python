def unit_converter():
    print("which converstion would you like?")
    print("1, kilometer to miles")
    print("2, miles to kilometer")
    choice = input ("enter 1 or 2 :")

    if choice == '1':
       value = float (input("enter value kilometers:"))
       result = value * 0.621371
       print(f"{value} kilometers is {result:.2f} miles.")
    elif choice == '2':
       value = float (input("enter value miles:"))
       result = value/0.621371
       print(f"{value} miles is {result:.2f} kilometers.")
    else:#if the user enter strings or numbers that doesn't exist in the choice
        print("invalid choice.")
unit_converter()