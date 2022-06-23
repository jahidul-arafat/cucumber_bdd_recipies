# ------------------------- user-defined-datatype -------------------------------------
from behave import register_type
from parse_type import TypeBuilder

# user-defined-type:: <DRESS>
parse_dresses = TypeBuilder.make_choice(["shirts", "t-shirts"])
register_type(DRESS=parse_dresses)

# user-defined-type:: <PANT>
parse_pants = TypeBuilder.make_choice(["pants", "gowns"])
register_type(PANT=parse_pants)


# user-defined-type:: <NUMBER>
def parse_number(text):
    return int(text)


register_type(NUMBER=parse_number)

# ------------------------- step functions ------------------------------------------
from behave import given, when, then
from hamcrest import assert_that, greater_than_or_equal_to
from bag import Bag


@given(u'user is on shop')
def step_impl(context):
    bag = getattr(context, "bag", None)
    if not bag:
        context.bag = Bag()
    context.bag.categories = {} # we supposed not to define it here. Its already defined at Object level;.
    # seems to me to be a bug


@when(u'user purchases {count:NUMBER} {d:DRESS}')
def step_impl(context, count, d):
    assert count, isinstance(count, int)
    context.bag.add_item(d,count,"tops")


@when(u'user purchases {count:NUMBER} {p:PANT}')
def step_impl(context, count, p):
    assert count, isinstance(count, int)
    context.bag.add_item(p,count,"bottoms")


@then(u'user leaves the shop with purchased item')
def step_impl(context):
    assert_that(len(context.bag.list_all_items_in_bag()), greater_than_or_equal_to(2))
    print(context.bag.list_all_items_in_bag())
