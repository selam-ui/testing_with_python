# first we have to get users age and license status
age = int(input("enter your age"))
license_status = (input("do you have a driving license? (yes/no:)")). lower()
#the next step is nested if/else to check eligibility
if age>=18:
    if license_status == "yes":
        print("you are eligiable to drive.")
    else: 
        print("you are old enough but do not have a license.")
else:
    print("you are not enough old enough to drive.")