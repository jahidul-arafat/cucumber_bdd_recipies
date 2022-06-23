# -*- coding: UTF-8 -*-
"""
Feature: Data Type with Cardinality one or more (many, List<T>)

  @comma-sep
  Scenario: Many list, comma-separated
    Given I go to a meeting
    When I meet Alice, Bob, Jahid
    And I meet Potash
    Then the following persons are present:
      | name   |
      | Alice  |
      | Bob    |
      | Jahid  |
      | Potash |

  @and-sep
  Scenario: Many list with list-separator "and"
    Given I go to a meeting
    When I meet Alice and Bob and Jahid
    Then the following persons are present:
      | name  |
      | Alice |
      | Bob   |
      | Jahid |
"""

"""
* collects all the positional arguments in a tuple.

** collects all the keyword arguments in a dictionary.

>>> def functionA(*a, **kw):
       print(a)
       print(kw)


>>> functionA(1, 2, 3, 4, 5, 6, a=2, b=3, c=5)
Output: *a-> (1, 2, 3, 4, 5, 6)
        **kw-> {'a': 2, 'c': 5, 'b': 3}
"""

# ----------------------- @mark.user_defined_types -------------------------
from behave import register_type
from parse_type import TypeBuilder

parse_person = TypeBuilder.make_choice(["Alice", "Bob", "Jahid", "Potash"])


# separator:: <and>
parse_persons_sep_and = TypeBuilder.with_many(parse_person, listsep="and")
register_type(PersonAndMore=parse_persons_sep_and)

# separator:: <,>
parse_persons_sep_comma = TypeBuilder.with_many(parse_person, listsep=",")
register_type(PersonCommaMore=parse_persons_sep_comma)

# ------------------------ @mark.steps -------------------------------------

from behave import given, when, then
from hamcrest import assert_that, contains
from meeting import Meeting

@given('I go to a meeting')
def step_impl(context):
    context.meeting = Meeting()


# -- MANY-VARIANT 1: Use Cardinality field in parse expression (comma-separated)
"""
Steps Covering
----------------
When I meet Alice, Bob, Jahid 
When I meet Potash
"""
@when('I meet {persons:PersonCommaMore}')
def step_impl(context, persons):
    for person in persons:
        context.meeting.persons.add(person)

"""
Steps Covering
----------------
When I meet Alice and Bob and Jahid 

"""
# -- MANY-VARIANT 2: Use special many data type ("and"-separated)
@when('I meet {persons:PersonAndMore}')
def step_impl(context, persons):
    for person in persons:
        context.meeting.persons.add(person)


@then('the following persons are present')
def step_impl(context):
    actual_persons = sorted(context.meeting.persons)  # sorted(set)--> returns a List
    expected_persons = sorted([row["name"] for row in context.table])

    # -- LIST-COMPARISON:
    assert_that(actual_persons, contains(*expected_persons))  # (list1, contains(*list2))

    print("Actual Persons: {}".format(actual_persons))
    print("Expected Persons: {}".format(expected_persons))
