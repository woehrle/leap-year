#Haley Woehrle, ONID 933345684
#cs362 HW3 - Leap Year Program


user_input = int(input("Enter a year: "))

if user_input % 4 == 0 and user_input % 100 != 0:
    print(str(user_input)+ " is a Leap Year!")
elif user_input % 100 != 0 and user_input % 400 ==0:
    print(str(user_input)+ " is a Leap Year!")
else:
    print(str(user_input) + " is NOT a Leap Year.")