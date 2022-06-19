from email.policy import strict
import string
from behave import given, when, then, step

@given(u'the input "{expression}"')
def step_impl(context,expression):
    context.expression=str(expression)

@when(u'the calculator is run')
def step_impl(context):
    context.output= eval(context.expression)

@then(u'the output should be "{expected_output:d}"')
def step_impl(context,expected_output):
    assert context.failed is False
    assert context.output == expected_output

