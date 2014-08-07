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
        database.insert_delta(name, dates.date_today(), delta, dbname)

	budg = database.get_budget(name, dbname)

	delt = (budget.get_day_delta(name, dates.date_today(), dbname),
        budget.get_week_delta(name, dates.date_today(), dbname),
        budget.get_month_delta(name, dates.date_today(), dbname))

	diff = budget.add_triple(budg, delt)

	return render_template("base.html", form = form,
        budget = budget.format_triple(budg),
        delta = budget.format_triple(delt),
        diff = budget.format_triple(diff),
        weekDayNumber = dates.week_day_num(dates.date_today()) + 1,
        monthDayNumber = dates.month_day_num(dates.date_today()) + 1,
        daysInMonth = dates.num_days_in_month(dates.date_today()),
        today = dates.date_today())
