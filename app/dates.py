import datetime, calendar

def dateToday():
	return datetime.date.today()

def datesThisWeek():
	today = dateToday()
	weeks = calendar.Calendar(0).monthdatescalendar(today.year, today.month)
	for week in weeks:
		for d in week:
			if d == today:
				return week

def datesThisMonth():
	today = dateToday()
	weeks = calendar.Calendar(0).monthdatescalendar(today.year, today.month)
	days = []
	for week in weeks:
		for d in week:
			days.append(d)
	return days

def numDaysThisMonth():
	today = dateToday()
	dates = calendar.Calendar(0).itermonthdates(today.year, today.month)
	numDays = 0
	for d in dates:
		if d.month == today.month:
			numDays = numDays + 1
	return numDays

def numWeeksThisMonth():
	if numDaysThisMonth() % 7 > 0:
		return 4
	else:
		return 3

def daysLeftInWeek():
	for i, d in enumerate(datesThisWeek()):
		if d == dateToday():
			return 7 - i

def daysLeftInMonth():
	for i, d in enumerate(datesThisMonth()):
		if d == dateToday():
			return numDaysThisMonth() - i

if __name__ == "__main__":
	print daysLeftInWeek()
	print daysLeftInMonth()