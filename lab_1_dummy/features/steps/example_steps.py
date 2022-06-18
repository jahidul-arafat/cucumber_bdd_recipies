from behave import given, when, then, step

@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement {number:d} tests')
def step_impl(context, number):
    assert number >= 1
    context.test_count=number 


@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False # The assertion condition context.failed is False will become false if an error has occurred in an earlier feature (or scenario). Therefore, it will be expected behavior that the AssertionError is raised if an error has occurred.
    assert context.test_count >=1