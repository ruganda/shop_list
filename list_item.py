import time
class ListItem(object):
	def __init__(self,name):
		self.name=name
		self.complete_status=False
		self.date_completed=""

	def show_info(self):
		return {"name":self.name,"complete_status":self.complete_status}

	def mark_complete(self):
		self.complete_status=True
		self.date_completed=time.strftime("%d/%m/%Y")+" "+time.strftime("%I:%M:%S")