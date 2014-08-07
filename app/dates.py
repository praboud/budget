"""
Helper functions for abstracting datetime and calendar modules.
Jake Pittis 2014
"""

import datetime, calendar

def date_today():
	""" Returns todays date object.

	Access todays date without importing the datetime module.
	"""
	return datetime.date.today()

def dates_in_week(date):
	"""Returns a list of date objects for the week of the given date object.

	Weeks start on Monday. If week overlaps two months,
	list will include dates from both months.
	"""
	weeks = calendar.Calendar(0).monthdatescalendar(date.year, date.month)
	for week in weeks:
		for d in week:
			if d == date_today():
				return week

def dates_in_month(date):
	"""Returns a list of date objects for the month of given date object.

	List will only include dates from given month.
	"""
	weeks = calendar.Calendar(0).monthdatescalendar(date.year, date.month)
	days = []
	for week in weeks:
		for d in week:
			days.append(d)
	return days

def num_days_in_month(date):
	"""Returns the number of days in the month of given date object.

	Will always return between 28 and 31.
	"""
	dates = calendar.Calendar(0).itermonthdates(date.year, date.month)
	numDays = 0
	for d in dates:
		if d.month == date_today().month:
			numDays = numDays + 1
	return numDays

def num_weeks_in_month(date):
	"""Returns the number of weeks in the month of given date object.

	Will always return 3 or 4.
	"""
	if num_days_in_month(date) % 7 > 0:
		return 4
	else:
		return 3

def week_day_num(date):
	"""Return the week day number for given date object.

	Where Monday is 0 and Sunday is 6.
	"""
	for i, d in enumerate(dates_in_week(date)):
		if d == date_today():
			return i

def month_day_num(date):
	"""Return the month day number for given date object.

	Where the first day of the month is 0.
	"""
	return date.day - 1