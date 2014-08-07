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