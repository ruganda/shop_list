
from .shoppinglist import shoppinglist
class User(object):
	"""
		The user class implements the functionality of a user on the shoppinglist application
	"""
	def __init__(self,first_name,last_name,email,password):
		"""The constructor initialises class variables"""
		self.name=first_name+" "+last_name
		self.email=email
		self.password=password
		self.shoppinglists={}
		self.login_status=False

	def login(self,email,password):
		"""The login method checks if the user email and password match the ones provided by the app"""
		if email==self.email and password==self.password:
			self.login_status=True
			return True
		else:
			print(self.email)
			print(self.password)
			return False

	def get_info(self):
		"""This method rreturns a dictionary of user info"""
		pass

	def logout(self,email,password):
		""" The logout method toggles the login status to off"""
		pass

	def add_shoppinglist(self,name,item_number):
		""" This method adds a new shoppinglist"""
		self.shoppinglists[name]=shoppinglist(name,item_number)

	def view_shoppinglist(self,name=""):
		"""This method returns a dictionary of cart list elements"""
		if name and name in self.shoppinglists:
			shoppinglist=self.shoppinglists[name]
			return {"name":shoppinglist.name,"item_number":shoppinglist.item_number}
		elif not name:
			return self.shoppinglists
		elif name not in self.shoppinglists:
			return False

	def edit_shoppinglist(self,cart,name,item_number):
		"""This method edits the shoppinglist specified"""
		if cart in self.shoppinglists:
			return cart.edit(name,item_number)
		else:
			return False

	def edit_shoppinglist_item(self,cart,old_name,new_name):
		"""This edits an item in the shoppinglist"""
		if cart in self.shoppinglists:
			conataining_cart=self.shoppinglists[cart]
			edit_this=conataining_cart.get_item(old_name)
			return conataining_cart.edit_item(edit_this,new_name)
		else:
			return False

	def add_shoppinglist_item(self,shoppinglist,item_name):
		"""This method edits the shoppinglist specified"""
		if shoppinglist in self.shoppinglists:
			cart=self.shoppinglists[shoppinglist]
			cart.add_item(item_name)
			if item_name in cart.shoppinglist_items:
				return cart.view_item(item_name)
			else:
				return False
		else:
			return False

	def mark_complete(self,shoppinglist,item):
	 	"""Mark item as complete"""
	 	if shoppinglist in self.shoppinglists:
	 		cart=self.shoppinglists[shoppinglist]
	 		completed=cart.complete_item(item)
	 		if completed:
	 			return completed
 			else:
 				return False

	def view_cart_list_item(self,shoppinglist,item_name=""):
		if shoppinglist in self.shoppinglists:
			items=[]
			cart=self.shoppinglists[shoppinglist]
			if item_name:
				last=cart.get_item(item_name)
				if last:
					items.append(last)
			else:
				res=cart.view_shoppinglists()
				for itm in res:
					last=cart.get_item(itm)
					if last:
						items.append(last)
			return items
		else:
			return False

	def delete_shoppinglist(self,name):
		if name in self.shoppinglists:
			del self.shoppinglists[name]
		else:
			return "cart list not deleted"

	def delete_shoppinglist_item(self,bklist,name):
		if bklist in self.shoppinglists:
			res=self.shoppinglists[bklist].delete_item(name)
			return res
		else:
			return False



