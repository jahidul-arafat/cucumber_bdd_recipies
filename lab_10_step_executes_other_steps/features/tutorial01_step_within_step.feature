Feature: Step executes other steps (tutorial10)
    @scenario_01
    Scenario: Step by Step
        Given I start a new game 
        When I press the big red button
        And I duck 
        Then I reach the next level
        
    @scenario_02
    Scenario: Execute multiple Steps in middle step
        Given I start a new game
        When I do the same thing as before 
        Then I reach the next level

