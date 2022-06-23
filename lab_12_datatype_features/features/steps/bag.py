"""
Check whether an attribute is in an object
>>> class new_class():
...   def __init__(self, number):
...     self.multi = int(number) * 2
...     self.str = str(number)
...
>>> a = new_class(2)
>>> a.__dict__
{'multi': 4, 'str': '2'}
>>> a.__dict__.keys()
dict_keys(['multi', 'str'])

"""

class Bag(object):
    def __int__(self):
        self.categories = {}

    def add_item(self, item_name, count, cat_name):
        if cat_name not in self.categories:
            self.categories[cat_name] = []

        assert (item_name, count) not in self.categories[cat_name]
        self.categories[cat_name].append((item_name, count))

    def get_item_count_for(self, cat_name):
        return len(self.categories[cat_name])

    def list_all_items_in_bag(self):
        return self.categories.values()
