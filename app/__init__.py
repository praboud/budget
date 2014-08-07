from flask import Flask, render_template, url_for, request
from flask_wtf import Form
from wtforms import FloatField
from app import budget, database, dates

app = Flask(__name__)

import os
app.config["SECRET_KEY"] = os.urandom(24)
del os

database.init(10, 20, 50)

class Budget(Form):
	deposit = FloatField("Save", default = 0)
 	withdraw = FloatField("Spend", default = 0)

@app.route("/", methods = ["GET", "POST"])
def base():
	form = Budget()
	deposited = 0
	withdrawn = 0
	if request.method == 'POST':
		# update database values
		withdrawn = form.withdraw.data or 0
		deposited = form.deposit.data or 0
        delta = deposited - withdrawn
        database.insertTransaction(delta, dates.dateToday())
	return render_template("base.html", form = form,
        budget = budget.budgets(),
        delta = budget.deltas(),
        today = dates.dateToday(),
        daysLeftWeek = dates.daysLeftInWeek(),
        daysLeftMonth = dates.daysLeftInMonth(),
        daysInMonth = dates.numDaysThisMonth())
