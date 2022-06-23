# user-defined-datatype
from behave import register_type
from parse_type import TypeBuilder


#white-spaces
def slurp_space(text):
    return text
slurp_space.pattern = r"\s*" # zero or more occurance of white spaces
register_type(slurp_space=slurp_space)

# COLOR
parse_color = TypeBuilder.make_choice(["red","green","blue","yellow"])
register_type(Color=parse_color)

#  parse_color:: and-sep
parse_color_and_sep = TypeBuilder.with_zero_or_more(parse_color, listsep="and")
register_type(OptionalColorAndMore = parse_color_and_sep)

# parse_color:: comma-sep
parse_color_comma_sep = TypeBuilder.with_zero_or_more(parse_color,listsep=",")
register_type(OptionalColorCommaMore = parse_color_comma_sep)

# step functions
from behave import given, when, then
from hamcrest import assert_that, contains, has_length

@given(u'I am a painter')
def step_impl(context):
    context.used_colors = set()


@when(u'I paint with{:slurp_space}{colors:OptionalColorCommaMore}') #slurp is needed for this step mostly
def step_impl(context,_,colors):
    for color in colors:
        context.used_colors.add(color)


@when(u'I paint with{:slurp_space}{colors:OptionalColorAndMore}')
def step_impl(context,_,colors):
    for color in colors:
        context.used_colors.add(color)

@then(u'no colors are used')
def step_impl(context):
    assert_that(context.used_colors,has_length(0))


@then(u'the following colors are used')
def step_impl(context):
    used_colors = sorted(context.used_colors)
    expected_colors = sorted([row["color"] for row in context.table])

    # list-comparison
    assert_that(used_colors,contains(*expected_colors))

    print(context.table)
    print("used_colors:{}".format(used_colors))
    print("expected_colors:{}".format(expected_colors))




