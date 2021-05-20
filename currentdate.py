# This program displays current date and time.

import datetime

date = datetime.datetime.now().date()
time = datetime.datetime.now().time()
print("Today's date is ", date, " and time is ", time)
