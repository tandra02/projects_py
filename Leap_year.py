def check_leap_year(year):
   if year % 4 == 0:
       print(f"\n{year} is a leap year.")
       seconds = float(366*3600*24)
       print(f"\n{year} has {seconds} second.\n")
   else:
       print(f"\n{year} is not a leap year.")
       seconds = float(365*3600*24)
       print(f"\n{year} has {seconds} seconds.\n")
        
year = int(input("Enter a year >\n"))
if year <= 0:
    year_again = int(input("Enter a positive year >\n"))
else:
    check_leap_year(year)