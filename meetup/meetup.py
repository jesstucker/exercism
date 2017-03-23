def meetup_day(year, month, weekday, place_in_month):
	# example: meetup_day(2013, 5, 'Monday', 'teenth')
	from datetime import date
	import calendar

	teenth = ['13','14','15','16','17','18','19']

	cal = calendar.Calendar()
	monthdates = cal.itermonthdates(year, month)

	possible_dates = []
	for monthdate in monthdates:
		if monthdate.strftime("%A") == weekday and monthdate.strftime("%-m") == str(month):
	   		possible_dates.append(monthdate.strftime("%d"))
	# return possible_dates

	if   place_in_month == "1st":
		day = possible_dates[0]
	elif place_in_month == "2nd":
		day = possible_dates[1]
	elif place_in_month == "3rd":
		day = possible_dates[2]
	elif place_in_month == "4th":
		day = possible_dates[3]
	elif place_in_month == "5th":
		day = possible_dates[4]
	elif place_in_month == "last":
		day = possible_dates[-1]
	elif place_in_month == "teenth":
		day = [teen_day for teen_day in teenth if teen_day in possible_dates][0]
	day = int(day)
		
	return date(year, month, day)



	# days = list(calendar.day_name)
	# place = ['1st','2nd','3rd','4th','5th', 'last','teenth']

	# days_in_month = calendar.monthrange(year,month)[1]

		



	# day = the weekday that fits place_in_month
	# return date(year, month, day)