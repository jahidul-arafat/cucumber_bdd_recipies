"""
Feature: Fight or Flight (Lab04/Natual Language/Ninja)
    In order to increase the ninja survival rate,               #< Business goal
    As a ninja commander                                        #< Role
    I want my ninjas to decide whether to take on an opponent   #< Benefit
    based on their skill levels.

    Scenario: Weaker opponent
        Given the ninja has a third level black-belt
        When attacked by a samurai
        Then the ninja should engage the opponent 

    Scenario: Stronger opponent
        Given the ninja has a third level black-belt
        When attacked by Chuck Norris
        Then the ninja should run for his life
"""
"""
> behave lab_4_natural_language/features/tutorial01_ninja.feature --dry-run
> behave lab_4_natural_language/features/tutorial01_ninja.feature
1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.000s
"""

from behave import given, when, then                    # pip install behave
from hamcrest import assert_that, equal_to, is_not      # pip install pyhamcrest


#--------------------------------------------------------------------------------
# PROBLEM DOMAIN:
#--------------------------------------------------------------------------------

class NinjaFight(object):
    def __init__(self, with_ninja_level):
        self.with_ninja_level = with_ninja_level 
        self.opponent = None 
    
    def decision(self):
        # Business logic for a Ninja should react to increase his survival rate
        assert self.with_ninja_level is not None
        assert self.opponent is not None
        if self.opponent == "Chuck Norris":
            return "run for his life"
        else:
            return "engage the opponent"


#--------------------------------------------------------------------------------
# STEPS:
#--------------------------------------------------------------------------------
@given(u'the ninja has a {achievement_level}')
def step_impl(context, achievement_level):
    context.ninja_fight = NinjaFight(achievement_level) # Define the class


@when(u'attacked by a {opponent_weapon}')
def step_impl(context,opponent_weapon):
    context.ninja_fight.opponent=opponent_weapon

@when(u'attacked by {opponent_person}')
def step_impl(context,opponent_person):
    context.ninja_fight.opponent=opponent_person

@then(u'the ninja should {reaction}')      
def step_impl(context,reaction):
    assert_that(reaction,equal_to(context.ninja_fight.decision()))