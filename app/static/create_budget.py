# what is this doing here?
import sqlite3

db = sqlite3.connect('budget.db')
c = db.cursor()
c.execute('''DROP TABLE IF EXISTS budget''')
c.execute('''CREATE TABLE IF NOT EXISTS toppings (
	id INT PRIMARY KEY NOT NULL,
	month-budget TEXT NOT NULL,
	month-current TEXT NOT NULL,
	week-budget TEXT NOT NULL,
	week-current TEXT NOT NULL,
	day-budget TEXT NOT NULL,
	day-current TEXT NOT NULL,
	)''')

day-budget = 10.00

extra-week-budget = 20.00
extra-month-budget = 100.00

week-budget = 7 * day-budget + extra-week-budget
month-budget = 30 * day-budget + extra-month-budget

c.execute('''INSERT OR REPLACE INTO budget VALUES (?, ?, ?, ?, ?)''',
                (t, t, topping_name[i]))
