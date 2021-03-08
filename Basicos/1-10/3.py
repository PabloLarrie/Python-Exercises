# Write a Python program to display the current date and time.
# Sample Output:
# Current date and time :
# 2014-07-05 14:34:14


from datetime import datetime

mytime = datetime.now()
DATETIME_FMT = "%Y-%m-%d %H:%M:%S"

print(f"Current date and time : {mytime.strftime(DATETIME_FMT)}")
