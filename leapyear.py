def is_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year.")
        return True
    else:
        print("Not a leap year.")
        return False

year = int(input("Enter a year: "))

is_leapyear(year)