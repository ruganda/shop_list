import unittest
from app.models.list_item import ListItem

class test_shoppinglist_item(unittest.TestCase):
	def setUp(self):
		self.list_item=ListItem("Awesome")

	def test_add_create_item(self):
		self.assertIsInstance(self.list_item,ListItem,"List Item class not created")

	def test_complet_shoppinglist_item(self):
		self.list_item.mark_complete()
		self.assertTrue(self.list_item.show_info()['complete_status'])

	def test_show_info(self):
		self.list_item.mark_complete()
		info=self.list_item.show_info()
		self.assertDictEqual(info,{"name":"Awesome","complete_status":True})
	def test_show_info_returns_dictionary(self):
		info=self.list_item.show_info()
		self.assertIsInstance(info,dict,"Dictionary not returned")
