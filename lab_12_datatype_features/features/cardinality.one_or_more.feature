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