def days_of_month(month,year):
	days_31 = ['Jan','Mar','May','Jul','Aug','Oct','Dec']
	days_30 = ['Apr','Jun','Sept','Nov']
	if month in days_31:
		return 31
	elif month in days_30:
		return 30
	else:
		if(year%400 == 0) and (year%4 == 0):
			return(29)
		else:
			return(28)


days = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
year =[]
start_year,stop_year = 1900,2000
for i in range(start_year,stop_year+1):
	year.append(i)
days_passed =[]
day_count = 0
count_sundays = 0

for y in year:
	for m in months:
		for d in range(1,days_of_month(m,y)):
			days_passed.append(days[day_count])
			if (days_passed[-1] == 'Sun') and (d == 1) and (y != start_year):
				count_sundays+=1
			day_count+=1
			if(day_count == len(days)):
				day_count = 0
print(count_sundays)