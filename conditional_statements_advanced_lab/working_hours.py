working_hors = int(input())
day_of_week = input()
if day_of_week == "Sunday":
    print("closed")
if day_of_week == "Monday"\
        or day_of_week == "Tuesday"\
        or day_of_week == "Wednesday"\
        or day_of_week == "Thursday"\
        or day_of_week == "Friday"\
        or day_of_week == "Saturday":
    if working_hors >= 10 and working_hors <= 18:
        print("open")
    else:
        print("closed")