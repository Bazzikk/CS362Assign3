
# To verify if a year is a leap year
def leapYearVerifier (year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print("It is a leap year")
            else:
                print("Not a leap year")

        else:
            print("It is a leap year")

    else:
        print("Not a leap year")




# Enter year to verify
val = input("Enter year: ")


# Verifying val is a number
while not(type(val) == type(0)):
    try:
      val = int(val)
    except:
      print("Error: Invalid Input")
      val = input("Enter year: ")

# Converting val if negative into a positive number
if val < 0:
    val = val * -1
    print("Notice: Converted into a positive number")

print("Verifying if year {} is a leap year".format(val))

leapYearVerifier(int(val))
