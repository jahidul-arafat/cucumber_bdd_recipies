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

from behave import given, when, then
from hamcrest import assert_that, equal_to
from blender import Blender

@given(u'I put "{thing}" in a blender')
def step_impl(context,thing):
    context.blender = Blender()
    context.blender.add(thing)


@when(u'I switch the blender on')
def step_impl(context):
    context.blender.switch_on()


@then(u'it should transform into "{other_thing}"')
def step_impl(context,other_thing):
    assert_that(context.blender.result, equal_to(other_thing))