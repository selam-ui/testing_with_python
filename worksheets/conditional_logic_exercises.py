#first we get current time from user
hour= int(input("enter the current hour (0-23):"))
#then we write the condition logic
if hour < 12 :
    print("GOOD MORNING!, Have a great day")
elif hour < 18 :
    print("GOOD AFTERNOON!, Hope your day is going well!")
elif hour < 21 :
    print("GOOD EVENING!, Relax and enjoy ")
else:
    print("GOOD NIGHT, Sleep well and sweet dreams")