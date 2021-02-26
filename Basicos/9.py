# Write a Python program to display the examination schedule. 
# (extract the date from exam_st_date). exam_st_date = (11, 12, 2014)

exam_st_date = (26, 12, 2021)
if exam_st_date[1] == 12 : month = "Diciembre"

print(f"El examen será el día {exam_st_date[0]} de {month} de {exam_st_date[-1]}")