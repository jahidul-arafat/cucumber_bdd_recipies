from behave import given, when, then
from hamcrest import assert_that, has_items
from hamcrest.library.collection.issequence_containinginanyorder import contains_inanyorder
import collections
from company_model import CompanyModel

"""
Python getattr() function is used to access the attribute value of an object 
and also gives an option of executing the default value in case of unavailability of the key.

Here,   object      :   <context>
        attribute   :   <model>
- Check it the arrtibute <model> is already exists.
- If not, then create the attribute

Example:

# declaring class
class GfG:
    name = "GeeksforGeeks"
    age = 24
 
# initializing object and
# python getattr() function call
obj = GfG()
 
# use of getattr
print("The name is " + getattr(obj, 'name'))
 
# use of getattr with default
print("Description is " + getattr(obj,
                                  'description',
                                  'CS Portal'))
 
# use of getattr without default
print("Motto is " + getattr(obj, 'motto'))

Output: 
-------------

The name is GeeksforGeeks
Description is CS Portal
Exception: 

AttributeError: GfG instance has no attribute 'motto'

"""
@given(u'a set of specific users')
def step_impl(context):
    model = getattr(context, "model",None)
    if not model:
        context.model = CompanyModel()
    for row in context.table:
        context.model.add_user(row["name"], row["department"])

@then(u'we will have the following people in "{department}"')
def step_impl(context,department):
    if department not in context.model.departments:
        assert_that(False, "Department {}  is unknown".format(department))
    
    expected_persons = [row["name"] for row in context.table]
    actual_persons = context.model.departments[department]

    compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
    assert compare(expected_persons,actual_persons)

@then(u'we will have at least the following people in "{department}"')
def step_impl(context,department):
    if department not in context.model.departments:
        assert_that(False, "Department {} is unknown".format(department))
    
    at_least_these_persons = [row["name"] for row in context.table]
    actual_persons_main_collection = context.model.departments[department]

    # assert_that([1,2,3],has_items(*[1,4])) --> False 
    # assert_that(main_collection::LIST, has_items(*at_least_these_items_should_be_in_list::LIST))
    assert_that(actual_persons_main_collection,has_items(*at_least_these_persons))

