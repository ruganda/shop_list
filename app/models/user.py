
from .shoppinglist import ShoppingList


class User(object):
    """
            The user class implements the functionality of a user on the shoppinglist application
    """

    def __init__(self, first_name, last_name, email, password):
        """The constructor initialises class variables"""
        self.name = first_name + " " + last_name
        self.email = email
        self.password = password
        self.shoppinglists = {}
        self.login_status = False

    def login(self, email, password):
        """The login method checks if the user email and password match the ones provided by the app"""
        if email == self.email and password == self.password:
            self.login_status = True
            return True
        else:
            print(self.email)
            print(self.password)
            return False

    def get_info(self):
        """This method rreturns a dictionary of user info"""
        pass

    def logout(self, email, password):
        """ The logout method toggles the login status to off"""
        pass

    def add_shoppinglist(self, name, shopping):
        """ This method adds a new shoppinglist"""
        self.shoppinglists[name] = ShoppingList(name, shopping)

    def view_shoppinglist(self, name=""):
        """This method returns a dictionary of shopping list elements"""
        if name and name in self.shoppinglists:
            shoppinglist = self.shoppinglists[name]
            return {"name": shoppinglist.name, "shopping": shoppinglist.Items}
        elif not name:
            return self.shoppinglists
        elif name not in self.shoppinglists:
            return False

    def edit_shoppinglist(self, shopping, name,):
        """This method edits the shoppinglist specified"""
        if shopping in self.shoppinglists:
            return shopping.edit(name, shopping)
        else:
            return False

    def edit_shoppinglist_item(self, shopping, old_name, new_name):
        """This edits an item in the shoppinglist"""
        if shopping in self.shoppinglists:
            conataining_shopping = self.shoppinglists[shopping]
            edit_this = conataining_shopping.get_item(old_name)
            return conataining_shopping.edit_item(edit_this, new_name)
        else:
            return False

    def add_shoppinglist_item(self, shoppinglist, item_name):
        """This method edits the shoppinglist specified"""
        if shoppinglist in self.shoppinglists:
            shopping = self.shoppinglists[shoppinglist]
            shopping.add_item(item_name)
            if item_name in shopping.shoppinglist_items:
                return shopping.view_item(item_name)
            else:
                return False
        else:
            return False

    def mark_complete(self, shoppinglist, item):
        """Mark item as complete"""
        if shoppinglist in self.shoppinglists:
            shopping = self.shoppinglists[shoppinglist]
            completed = shopping.complete_item(item)
            if completed:
                return completed
            else:
                return False

    def view_shopping_list_item(self, shoppinglist, item_name=""):
        if shoppinglist in self.shoppinglists:
            items = []
            shopping = self.shoppinglists[shoppinglist]
            if item_name:
                last = shopping.get_item(item_name)
                if last:
                    items.append(last)
            else:
                res = shopping.view_shoppinglists()
                for itm in res:
                    last = shopping.get_item(itm)
                    if last:
                        items.append(last)
            return items
        else:
            return False

    def delete_shoppinglist(self, name):
        if name in self.shoppinglists:
            del self.shoppinglists[name]
        else:
            return "Shopping list not deleted"

    def delete_shoppinglist_item(self, bklist, name):
        if bklist in self.shoppinglists:
            res = self.shoppinglists[bklist].delete_item(name)
            return res
        else:
            return False
