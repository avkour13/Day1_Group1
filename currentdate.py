# This program displays current date and time.

import datetime


def fetch_date():
    date_today = datetime.datetime.now().date()
    return date_today


def fetch_time():
    time_now = datetime.datetime.now().time()
    return time_now


def print_datetime():
    date = fetch_date()
    time = fetch_time()
    print("Today's date is ", date, " and time is ", time)


print_datetime()
