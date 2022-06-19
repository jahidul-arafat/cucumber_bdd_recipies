Feature: Step Setup Table (lab_8/database)

    Scenario: Setup Table in Database
        Given a set of specific users:
            | name      | department  |
            | Barry     | IT          |
            | Pudey     | Marketing   |
            | Bekar     | Marketing   |
        When we count the number of people in each department 
        Then we will find two person in "Marketing" department
        AND we will find one person in "IT" department