import unittest
import context
from app.models import user

class TestUser(unittest.TestCase):
	"""Class to test for user class functionality"""
	def setUp(self):
		"""Setup a user instance to be used for testing throughout the app"""

		self.test_user=user.User("ruganda","mubarak","muba@gmail.com","15december")
	def test_user_assigned_name(self):
		"""Testing if a user is assigned a name"""
		self.assertEqual(self.test_user.name,"ruganda mubarak","User name not initialized")

	def test_user_created(self):
		"""Testing if an instance of User objest has been created"""
		self.assertIsInstance(self.test_user,user.User,"User object has not been instatiated")

	def test_user_password(self):
		"""Testing if user has been assigned a password"""
		self.assertEqual(self.test_user.password,"15december","User has not been assigned a password")

	def test_user_assigned_email(self):
		"""Testing if user has been assigned an email"""
		self.assertEqual(self.test_user.email,"muba@gmail.com","User not assigned email")

	def test_user_login(self):
		"""Testing if the login function starts"""
		logged_in=self.test_user.login("muba@gmail.com","15december")
		self.assertTrue(logged_in,"User not able to login")


	def test_add_shoppinglist(self):
		cart_lists=self.test_user.view_shoppinglist()
		len1=len(cart_lists)
		self.test_user.add_shoppinglist("funiture",30)
		new_cart_lists=self.test_user.view_shoppinglist()
		len2=len(new_cart_lists)
		self.assertNotEqual(len2,len1,"shoppinglist not added")

	def test_view_shoppinglist(self):
		self.test_user.add_shoppinglist("funiture",30)
		cart_list=self.test_user.view_shoppinglist("funiture")
		self.assertDictEqual({"name":"funiture","itemnumber":30},cart_list,"cart list not returned")


	def test_delete_cart_list(self):
		self.test_user.add_shoppinglist("My shoppinglist",40)
		cart_lists1=self.test_user.view_shoppinglist("My shoppinglist")
		len1=len(cart_lists1)
		self.test_user.delete_shoppinglist("My shoppinglist")
		cart_lists2=self.test_user.view_shoppinglist()
		len2=len(cart_lists2)
		self.assertNotEqual(len2,len1,"cart list has not been deleted")