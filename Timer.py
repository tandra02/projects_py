from datetime import datetime

print("\n\t Event Countdown Timer")
print("-" * 45)
year = int(input("\nInput the year (yyyy) > "))
month = int(input("Input the month (mm) > "))
day = int(input("Input the day (dd) > "))

today = datetime.now().date()
birthday = datetime(year, month, day).date()

if today == birthday:
    print("\nToday is your birthday!")
else:
    new_date = (birthday - today).days
    if new_date > 0:
        print("\nComing soon")
        print(f"You have {new_date} days left\n")
    else:
        print("\nNext year.")
        print(f"You have {-new_date} days left\n")
