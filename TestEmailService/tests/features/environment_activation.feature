Feature: Environment activation

  Scenario: Initial activation
    Given I am on the landing page
    Then I requested a new environment
    And Environment is not created yet
    When I click an activation link from the email
    Then I was redirected to the customer environment instance login page
    And I am receiving an email that confirms environment creation

  Scenario: Second activation
    Given I am on the landing page
    Then I requested an environment which already exist
    And Environment is already created
    When I click an environment link from email
    Then I was redirected to the customer environment instance login page

  Scenario: Unsuccessful request
    Given I am on the landing page
    When I submit missing customer information
    Then My request is not fulfilled
    And Environment creation was not triggered
    And I don't recieve any emails
