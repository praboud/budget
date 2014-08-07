import dates, database

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