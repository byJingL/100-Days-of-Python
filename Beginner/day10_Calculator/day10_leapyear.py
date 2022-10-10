def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(input_year, input_month):
    leap_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    not_leap_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(input_year):
        return leap_month_days[input_month-1]
    return not_leap_month_days[input_month-1]
  
  
#🚨 Do NOT change any of the code below 
a = int(input("Enter a year: "))
b = int(input("Enter a month: "))
days = days_in_month(a, b)
print(days)