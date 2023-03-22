import calendar

# print(calendar.MONDAY)
# print(calendar.TUESDAY)
# print(calendar.WEDNESDAY)
# print(calendar.THURSDAY)
# print(calendar.FRIDAY)
# print(calendar.SATURDAY)
# print(calendar.SUNDAY)

print(calendar.calendar(2023))
calendar.prcal(2020)



print(calendar.month(2002, 10))
calendar.prmonth(2002, 10)


calendar.setfirstweekday(calendar.SUNDAY)


print(calendar.weekday(2002, 10, 11))


print(calendar.weekheader(3))


print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021))



c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")


c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")


c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")


c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)

"""calendar.Calendar: proporciona métodos para preparar datos de calendario y dar formato.
calendar.TextCalendar: se utiliza para crear calendarios de texto regulares.
calendar.HTMLCalendar: se utiliza para crear calendarios HTML.
calendar.LocalTextCalendar: es una subclase de la clase calendar.TextCalendar. El constructor de esta clase toma el parámetro locale, el cual se utiliza para devolver los nombres apropiados de los meses y días de la semana.
calendar.LocalHTMLCalendar: es una subclase de la clase calendar.HTMLCalendar. El constructor de esta clase toma el parámetro "locale", que se usa para devolver los nombres apropiados de los meses y días de la semana."""