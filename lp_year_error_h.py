
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

print("Verifying if year {} is a leap year".format(val))

leapYearVerifier(int(val))
