Feature: Data Type with Cardinality zero or more
  Scenario: Empty list, comma-separated
    Given I am a painter
    When I paint with
    Then no colors are used

  Scenario: List with one item, comma-separated
    Given I am a painter
    When I paint with blue
    Then the following colors are used:
      | color |
      | blue  |

  Scenario: Many list, comma-separated
    Given I am a painter
    When I paint with red, green
    Then the following colors are used:
      | color |
      | red   |
      | green |

  Scenario: Many list, and-separated
    Given I am a painter
    When I paint with red and green and blue
    Then the following colors are used:
      | color |
      | red   |
      | green |
      | blue  |


# behave --no-capture -f plain lab_12_datatype_features/features/cardinality.zero_or_more.feature