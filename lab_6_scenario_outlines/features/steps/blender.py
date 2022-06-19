"""
Scenario Outline: Use Blender with <thing>
        Given I put "<thing>" in a blender
        When I switch the blender on
        Then it should transform into "<other thing>"

        Examples: Amphibians
            | thing         | other thing |
            | Red Tree Frog | mush        |
            | apples        | apple juice |

        Examples: Consumer Electronics
            | thing         | other thing |
            | iPhone        | toxic waste |
            | Galaxy Nexus  | toxic waste |

"""

class Blender(object):
    # Class Variable
    TRANSFORMATION_MAP={
        "Red Tree Frog":"mush",
        "apples":"apple juice",
        "iPhone":"toxic waste",
        "Galaxy Nexus":"toxic waste"
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