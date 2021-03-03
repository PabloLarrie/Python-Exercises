# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

c = calendar.TextCalendar(
    calendar.MONDAY
)  # Poner calendar.MONDAY es como no poner nada

strs = c.formatmonth(2021, 3)

print(strs)