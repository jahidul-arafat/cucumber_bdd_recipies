from behave import given, when, then
from hamcrest import assert_that, equal_to
from name2num import NamedNumber
from company_model import CompanyModel

@given(u'a set of specific users')
def step_impl(context):
    context.model = CompanyModel()
    for row in context.table:
        context.model.add_user(row["name"],row["department"])


@when(u'we count the number of people in each department')
def step_impl(context):
    pass

@then(u'we will find {count} person in "{department}" department')
def step_impl(context,count,department):
    count_ = NamedNumber.from_string(count)
    assert_that(
        count_,
        equal_to(context.model.get_headcount_for(department))
    )
