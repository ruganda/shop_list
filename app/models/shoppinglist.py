from .list_item import ListItem


class ShoppingList(object):
    def __init__(self, name, Items):
        self.name = name
        self.Items = Items
        self.shoppinglist_items = {}

    def get_info(self):
        pass

    def view_shoppinglists(self):
        return self.shoppinglist_items

    def edit(self, name, Items):
        self.name = name
        self.Items = Items
        return True

    def add_item(self, name):
        list_item = ListItem(name)
        self.shoppinglist_items[name] = list_item

    def edit_item(self, item, name):
        temp = item
        del self.shoppinglist_items[item.name]
        temp.name = name
        self.shoppinglist_items[name] = temp
        return temp.show_info()

    def delete_item(self, name):
        if name and name in self.shoppinglist_items:
            del self.shoppinglist_items[name]
            return True
        else:
            return False

    def complete_item(self, name):
        if name in self.shoppinglist_items:
            item = self.shoppinglist_items[name]
            item.mark_complete()
            return {"complete_status": item.complete_status, "date_completed": item.date_completed}
        else:
            return False

    def view_item(self, name):
        if name in self.shoppinglist_items:
            item = self.shoppinglist_items[name]
            return item.show_info()

    def get_item(self, name):
        if name in self.shoppinglist_items:
            item = self.shoppinglist_items[name]
            return item
        else:
            return False
