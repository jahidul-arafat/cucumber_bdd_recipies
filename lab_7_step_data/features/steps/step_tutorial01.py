from behave import given, when, then
from hamcrest import assert_that, equal_to
from frobulator import Frobulator

"""
# Check the behave context attributes: https://behave.readthedocs.io/en/stable/context_attributes.html

# getattr(
    obj: the object whose attribute need to be processed,
    key: the attribute of the object
    def: the default value that need to be printed in case attribute not found
    )
"""

@given(u'a sample text loaded into the frobulator')
def step_impl(context):
    # Check if the frobulator attribute is already decalded with object: context
    frobulator = getattr(context,"frobulator",None) 
    if not frobulator:
        context.frobulator = Frobulator()
    context.frobulator.text = context.text #< STEP-DATA from context.text

@when(u'we activate the frobulator')
def step_impl(context):
    context.frobulator.activate()


@then(u'we will find it similar to {language}')
def step_impl(context,language):
    assert_that (
                    language,
                    equal_to(context.frobulator.seems_like_language())
                )