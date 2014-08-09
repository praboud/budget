"""
Interface for sqlite3 database.
Jake Pittis 2014
"""

import sqlite3, dates

"""
Uses two tables, budgets and deltas.

budgets table
name text | day real | week real | month real

deltas table
id integer | budgetName text | date text | delta real
"""

# as you noted in your email, this is a bit basic, although it's quite sufficient
# for where the application is right now
# if you want to expand this, you may want to look into an ORM to abstract out
# database interactions
# I've only used the Django ORM, but it sounds like SQLAlchemy is another popular ORM
# for python

def create_tables(filename):
	"""Creates budgets and deltas tables if they do not already exist.

	Where filename is the database file name.
	"""
	db = sqlite3.connect(filename)
	c = db.cursor()

	c.execute('''CREATE TABLE IF NOT EXISTS budgets (
        name TEXT PRIMARY KEY,
        day REAL,
        week REAL,
        month REAL
        )''')

        # I was about to comment about using an SQL date datatype in this
        # table, but apparently sqlite doesn't have one...
        # that's pretty bush-league...
        # to be fair, sqlite is not really meant for any serious work
	c.execute('''CREATE TABLE IF NOT EXISTS deltas (
        id INTEGER PRIMARY KEY,
        budgetName TEXT,
        date TEXT,
        delta REAL,
        FOREIGN KEY(budgetName) REFERENCES budgets(name)
        )''')

	db.commit()

def drop_tables(filename):
	"""Removes budgets and deltas tables.

	Where filename is the database file name.
	"""
	db = sqlite3.connect(filename)
	c = db.cursor()

	c.execute('''DROP TABLE IF EXISTS budgets''')
	c.execute('''DROP TABLE IF EXISTS deltas''')

	db.commit()

def get_budget(name, filename):
	"""Returns the dayly, weekly and monthly budget.

	Where name is a primary key and filename is the database file name.
	"""
	db = sqlite3.connect(filename)
	c = db.cursor()

        # nice! all of this is SQL injection proof
        # I was almost disapointed ;)

	c.execute('''SELECT day, week, month FROM budgets WHERE name=?''',
	(name,))

	return c.fetchall()[0]

def get_total_delta(name, dates, filename):
	"""Returns the the sum of deltas from the dates provided.

	Where dates is a list of date objects.
	Where name is the budget name primary key.
	Where filename is the database file name.
	"""
	total_delta = 0

	db = sqlite3.connect(filename)
	c = db.cursor()

	for d in dates:
		c.execute('''SELECT delta FROM deltas WHERE date=? AND budgetName=?''',
			(d, name))
		detlas = c.fetchall()
		for d in detlas:
			total_delta = total_delta + d[0]

	return total_delta

def insert_budget(name, day, week, month, filename):
	"""Insert budget into budgets table.

	Where name is a primary key.
	Where day, week and month are floats.
	Where filename is the database filename.
	"""
	db = sqlite3.connect(filename)
	c = db.cursor()

	week = week + (7 * day)
	month = month + (week * dates.num_weeks_in_month(dates.date_today()))

	c.execute('''INSERT INTO budgets(name, day, week, month) VALUES(?, ?, ?, ?)''',
		(name, day, week, month))

	db.commit()

def insert_delta(name, date, delta, filename):
	"""Inserts a delta into deltas table.

	Where name is the budget primary key.
	Where date is a date object.
	Where delta is a float.
	Where filename is the database file name.
	"""
	db = sqlite3.connect(filename)
	c = db.cursor()

	c.execute('''INSERT INTO deltas(budgetName, date, delta) VALUES(?, ?, ?)''',
		(name, date, delta))

	db.commit()
