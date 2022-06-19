"""
Feature: Showing off behave (lab3_tutorial01)
    Scenario: Run a simple test
        Given we have behave installed
        When we implement a test
        Then behave will test it for us!
"""


from behave import given, when, then

@given(u'we have behave installed')
def step_impl(context):
    pass


@when(u'we implement a test')
def step_impl(context):
    assert True is not False  # Assert True passes if argument evaluate to true, which false does not


@then(u'behave will test it for us!')
def step_impl(context):
    assert context.failed is False