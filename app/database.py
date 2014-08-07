import sqlite3

def init(daylyBudget, weeklyBudget, monthlyBudget):
	createBudgetTable()
	createTransactionTable()
	db = sqlite3.connect("budget101.db")
	c = db.cursor()
	c.execute('''INSERT INTO budget(day, week, month) VALUES(?, ?, ?)''',
		(daylyBudget, weeklyBudget, monthlyBudget))
	db.commit()

def createBudgetTable():
	db = sqlite3.connect("budget101.db")
	c = db.cursor()
	c.execute('''DROP TABLE IF EXISTS budget''')
	c.execute('''CREATE TABLE IF NOT EXISTS budget (
        id INTEGER PRIMARY KEY NOT NULL,
        day REAL NOT NULL,
        week REAL NOT NULL,
        month REAL NOT NULL
        )''')
	db.commit()

def createTransactionTable():
	db = sqlite3.connect("budget101.db")
	c = db.cursor()
	c.execute('''DROP TABLE IF EXISTS deltas''')
	c.execute('''CREATE TABLE IF NOT EXISTS deltas (
        id INTEGER PRIMARY KEY NOT NULL,
        date TEXT NOT NULL,
        delta REAL NOT NULL
        )''')
	db.commit()

def monthBudget():
	db = sqlite3.connect("budget101.db")
	c = db.cursor()
	c.execute('''SELECT month FROM budget''')
	return c.fetchone()[0]

def weekBudget():
	db = sqlite3.connect("budget101.db")
	c = db.cursor()
	c.execute('''SELECT week FROM budget''')
	return c.fetchone()[0]

def dayBudget():
	db = sqlite3.connect("budget101.db")
	c = db.cursor()
	c.execute('''SELECT day FROM budget''')
	return c.fetchone()[0]

def transactionDelta(dates):
	delta = 0
	db = sqlite3.connect("budget101.db")
	c = db.cursor()
	for d in dates:
		c.execute('''SELECT delta FROM deltas WHERE date=?''', (d,))
		detlas = c.fetchall()
		for d in detlas:
			delta = delta + d[0]
	return delta

def insertTransaction(delta, date):
	db = sqlite3.connect("budget101.db")
	c = db.cursor()
	c.execute('''INSERT INTO deltas(date, delta) VALUES(?, ?)''', (date, delta))
	db.commit()

if __name__ == "__main__":
	init(10.00, 20.00, 60.00)
