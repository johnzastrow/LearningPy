import datetime


def print_header():
    print("-----------------------------------")
    print("        BIRTHDAY APP")
    print("-----------------------------------")
    print()


def get_birthday_from_user():
    print("Tell us when you were born: ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.datetime(year, month, day)
    return birthday


def compute_days_between_dates(bday, now):
    date1 = now
    date2 = datetime.datetime(now.year, bday.month, bday.day)
    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def print_birthday_information(days):
    if days < 0:
        print("Your birthday is in {} days!".format(-days))
    elif days > 0:
        print("You had your birthday already this year! {} days ago".format(days))
    else:
        print("Happy birthday!!!")


def print_age(bday, now):
    date1 = now
    date2 = datetime.datetime(bday.year, bday.month, bday.day)
    tdt = date1 - date2
    tdays = int(tdt.total_seconds() / 60 / 60 / 24)
    tyears = tdays / 365
    print("Your are", tdays, "days old")
    print("Your are", tyears, "years old")


def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)
    print_age(bday, now)


main()
