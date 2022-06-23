Feature: Multi Methods

  @male-user
  Scenario: Purchase-Shirt-Pant
    Given user is on shop
    When user purchases 3 shirts
    And user purchases 4 pants
    Then user leaves the shop with purchased item

  @female-user
  Scenario: Purchase-t_shirt-Gown
    Given user is on shop
    When user purchases 3 t-shirts
    And user purchases 4 gowns
    Then user leaves the shop with purchased item

    #behave --no-capture -f plain lab_12_datatype_features/features/multi_methods.feature
