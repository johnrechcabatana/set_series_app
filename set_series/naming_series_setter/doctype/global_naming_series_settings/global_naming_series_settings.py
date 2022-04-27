# Copyright (c) 2022, John Rech G. Cabatana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Globalnamingseriessettings(Document):
	def validate(self):
		if self.type_confirmed == "Confirmed":
			frappe.db.sql(""" UPDATE `tabSeries` set current =%s where name = %s""",(self.set_series,self.name_series ))
			self.set_series=0
			self.name_series=""
			self.type_confirmed=""
		else:
			frappe.msgprint("Please type/correct 'Confirmed'")
	pass
