from flask import Flask, render_template, url_for, request
from flask_wtf import Form
from wtforms import FloatField, TextField
from app import budget, database, dates

app = Flask(__name__)

import os
app.config["SECRET_KEY"] = os.urandom(24)
del os

dbname = "data.db"
database.drop_tables(dbname)
database.create_tables(dbname)
database.insert_budget("default", 10.00, 20.00, 50.00, dbname)

class Budget(Form):
	deposit = FloatField("Save", default = 0)
 	withdraw = FloatField("Spend", default = 0)

# overall comment about tabbing - python is whitespace sensitive
# general python convention seems to be that 1 indentation level = 4 spaces
# - not 1 tab character
# some of this code is mixing the use of tabs with the use of spaces, which
# can be super confusing, because tabs display as different width depending
# on how your editor is configured
# in most languages this is merely annoying / ugly, but in Python, it effects
# the meaning of the program.
# I'd highly recommend reformatting the code to 4 space indentation and sticking with it
# pep8 is a style checker for python, and will warn you about using tabs,
# among other style rules that it enforces

# nice discipline on sticking to having <80 characters per line!

@app.route("/", methods = ["GET", "POST"])
def base():
	form = Budget()

	name = "default"
	withdrawn = 0
	deposited = 0

	if request.method == 'POST':
		withdrawn = form.withdraw.data or withdrawn
		deposited = form.deposit.data or deposited
	delta = deposited - withdrawn

	# nice - good practice to not interact with the db directly in your controller logic
	database.insert_delta(name, dates.date_today(), delta, dbname)

	budg = database.get_budget(name, dbname)

	# this seems to be backwards: the delta will be positive if more
	# is saved than spent, but the summed deltas are reported as the amount
	# spent in the template
	delt = (budget.get_day_delta(name, dates.date_today(), dbname),
		budget.get_week_delta(name, dates.date_today(), dbname),
		budget.get_month_delta(name, dates.date_today(), dbname))

        # it might make sense to change the way you're grouping budget info
        # grouping it by delta/diff/budget and having a tuple to represent the
        # values for day/week/month is a bit awkward
        # I might suggest creating a class to represent a collection of budget data
        # this would encorporate the logic for collecting delta/diff/budget data about
        # a particular date period
        # you could, for bonus marks, abstract out the presentation logic as well
        # have a single template which displays delta/diff/budget, and include it in
        # your main template once for each date period
	diff = budget.add_triple(budg, delt)

	# if you wrap a method call across multiple lines, usual style is to indent
	# the extra lines for readability (there is some debate over how many
	return render_template("base.html", form = form,
	budget = budget.format_triple(budg),
		delta = budget.format_triple(delt),
		diff = budget.format_triple(diff),
		weekDayNumber = dates.week_day_num(dates.date_today()) + 1,
		monthDayNumber = dates.month_day_num(dates.date_today()) + 1,
		daysInMonth = dates.num_days_in_month(dates.date_today()),
		today = dates.date_today())
