# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.
import calendar
import datetime

validDate = True
MIN_YEAR = 1900
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

year = int(input("Please input the selected year: "))
month = int(input("Please input the selected month: "))
day = int(input("Please input the selected day: "))

# Get the year, then the month, then the day
# housekeeping()

# calculateLeapYear
def is_leap_year(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# Check to be sure date is valid

if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False

# validateDate leap year yes/no

elif (month == 2 and day > 29) if is_leap_year(year) else day > 28:
    validDate = False

# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
  print (f"{month}/{day}/{year} is a valid date")
    # Output statement
else:
  print (f"{month}/{day}/{year} is an invalid date")
    # Output statement
