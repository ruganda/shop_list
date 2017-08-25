import unittest
from app.models.shoppinglist import Shoppinglist
from app.models.list_item import ListItem

class TestShoppinglist(unittest.TestCase):
	def setUp(self):
		self.test_shoppinglist=Shoppinglist("cart1",30)

	def test_shoppinglist_created(self):
		self.assertIsInstance(self.test_shoppinglist,Shoppinglist,"shoppinglist class not instatiated")

	def test_shoppinglist_items_container(self):
		self.assertIsInstance(self.test_shoppinglist.view_shoppinglists(),dict,"Shoppinglist is not a dictionary")

	def test_shoppinglist_add_item(self):
		items_count=len(self.test_shoppinglist.view_shoppinglists())
		self.test_shoppinglist.add_item("table")
		increment=len(self.test_shoppinglist.view_shoppinglists())
		self.assertNotEqual(items_count,increment,"Item not added to shoppinglist")

	def test_edit_item(self):
		self.test_shoppinglist.add_item("chair")
		item=self.test_shoppinglist.get_item("chair")
		edited=self.test_shoppinglist.edit_item(item,"books")
		self.assertDictEqual(edited,{"name":"books","complete_status":False})


	def test_shoppinglist_complete_item(self):
		pass

	def test_shoppinglist_delete_item(self):
		pass

	def test_cart_list_name(self):
		pass

	def test_cart_list_due_age(self):
		pass

	def test_view_shoppinglist(self):
		pass

	def test_view_shoppinglist_items(self):
		pass

	def test_view_shoppinglist_item(self):
		self.test_shoppinglist.add_item("clothing")
		item=self.test_shoppinglist.view_item("clothing")
		self.assertEqual(item,{"name":"clothing","complete_status":False})

	def test_get_shoppinglist_item(self):
		self.test_shoppinglist.add_item("ball")
		item=self.test_shoppinglist.get_item("ball")
		self.assertIsInstance(item,ListItem,"List Item not added")


