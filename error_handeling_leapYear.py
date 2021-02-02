#Haley Woehrle, ONID 933345684
#cs362 HW3 - Leap Year Program - Error Handeling

#refrenced source https://www.youtube.com/watch?v=G3GAtoM3uq4

def isLeapYear(user_input):
  if (user_input % 4) == 0:
    if (user_input % 100) == 0:
      if (user_input % 400) == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

user_input = int(input("Enter a year: "))

if isLeapYear(user_input):
  print(str(user_input)+ " is a Leap Year! It contains 366 days.")
else:
  print(str(user_input) + " is NOT a Leap Year. It contains 365 days.")