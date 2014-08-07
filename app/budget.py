"""
Helper functions for abstracting the dates and database modules.
Jake Pittis 2014
"""

import dates, database, locale

def format(amount):
	"""Returns formated currency as string.

	Formated for United States and English Canada.
	"""
	locale.setlocale(locale.LC_ALL, "")
	return locale.currency(amount, grouping=True)

def format_triple(t):
	"""Returns a formated tuple in currency form.

	Requires a tuple of 3 numbers.
	"""
	return (format(t[0]), format(t[1]), format(t[2]))

def add_triple(a, b):
	"""Returns b subtracted from a.

	Requires a tuple of 3 numbers.
	"""
	return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def get_day_delta(name, date, filename):
	"""Returns total delta for date object."""
	return database.get_total_delta(name, [date], filename)

def get_week_delta(name, date, filename):
	"""Returns total delta for date objects week."""
	return database.get_total_delta(name, dates.dates_in_week(date), filename)

def get_month_delta(name, date, filename):
	"""Returns total delta for date objects month."""
	return database.get_total_delta(name, dates.dates_in_month(date), filename)