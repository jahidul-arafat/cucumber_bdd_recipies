"""
Scenario: Blenders
    Given I put "apples" in a blander
    When I switch the blander on 
    Then it should transform into "apple juice"

"""

class Blender(object):
    # Class Variable
    TRANSFORMATION_MAP={
        "apples":"apple juice"
    }

    # constructor, instance_method
    def __init__(self):
        self.thing=None
        self.result=None

    # as we are accessing the class_variable <TRANSFORMATION_MAP>, we need class method
    # Note: Class method is bound to class, not the object of the class. It can only access class variables.
    @classmethod
    def select_result_for(cls,thing):
        return cls.TRANSFORMATION_MAP.get(thing,"DIRT") # d.get(item,"if_item_not_found_in_dict_than_default_value")

    # instance method, having <self>
    def add(self,thing):
        self.thing=thing

    # instance method, having <self>
    def switch_on(self):
        self.result= self.select_result_for(self.thing)