# user-defined data type
from behave import register_type
def parse_number(text):
    return int(text)

register_type(Number=parse_number)

# Step functions
from behave import given, when, then
from hamcrest import assert_that, equal_to
from calculator import Calculator

@given(u'I have a calculator')
def step_impl(context):
    context.calculator = Calculator()


@when(u'I add "{x:Number}" and "{y:Number}"')
def step_impl(context, x, y):
    assert isinstance(x, int)
    assert isinstance(y, int)
    context.calculator.add2(x, y)


@then(u'the calculator returns "{expected:Number}"')
def step_impl(context, expected):
    assert isinstance(expected, int)
    assert_that(context.calculator.result, equal_to(expected))
