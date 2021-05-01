def week_days(day):
    print("The no. of day u entered is",day)

day_no = int(input("Enter day no."))

if day_no == 1:
    week_days("Monday") #calling function with MONDAY as input
elif day_no == 2:
    week_days("Tuesday")
elif day_no == 3:
    week_days("Wednesday")
elif day_no == 4:
    week_days("Thursday")
elif day_no == 5:
    week_days("Friday")
elif day_no == 6:
    week_days("Saturday")
elif day_no == 7:
    week_days("Sunday")