# first we have to get users input
name = input ("what is your name?")
favorite_food = input ("what is your favorite food?")
current_year = int(input ("what is the current year"))
age = int(input("how old are you?"))
birth_year= current_year - age
#then we print the greeting
print(f"hey {name}!,nice to meet you! i hope you have a great day.")
print(f"i see you are 20 years old and like {favorite_food}.")
#the final is calculate birth year of the user
birth_year = current_year - age 
print(f"you were probably born in {birth_year}.")