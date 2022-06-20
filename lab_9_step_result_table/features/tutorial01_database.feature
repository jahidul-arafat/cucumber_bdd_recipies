Feature: Step Result Table (tutorial07)

   Scenario: Unordered Result Table Comparison (RowFixture Table)
     Given a set of specific users:
        | name      | department  |
        | Alice     | IT          |
        | Bob       | IT          |
        | Jahid     | Sales       |
        | Dodo      | Sales       |
    Then we will have the following people in "Sales":
        | name    |
        | Jahid   |
        | Dodo    |
        
    And we will have the following people in "IT":
        | name    |
        | Bob     |
        | Alice   |


   Scenario: Subset Result Table Comparison
     Given a set of specific users:
        | name      | department       |
        | Jahid     | IT               |
        | Bob       | IT               |
    Then we will have at least the following people in "IT":
        | name    |
        | Bob     |