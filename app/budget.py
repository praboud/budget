"""
Helper functions for abstracting the dates and database modules.
Jake Pittis 2014
"""

import dates, database, locale

def format_money(amount):
	"""Returns formated currency as string.

	Formated for United States and English Canada.
	"""
	locale.setlocale(locale.LC_ALL, "")
	return locale.currency(amount, grouping=True)

def budgets():
	day = database.dayBudget()
	week = day * 7 + database.weekBudget()
	month = week * dates.numWeeksThisMonth() + database.monthBudget()
	return (day, week, month)

def deltas():
	day = database.transactionDelta([dates.dateToday()])
	week = database.transactionDelta(dates.datesThisWeek())
	month = database.transactionDelta(dates.datesThisMonth())
	return (day, week, month)

if __name__ == "__main__":
	print budgets()
	print deltas()