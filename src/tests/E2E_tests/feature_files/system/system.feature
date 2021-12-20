Feature: System should prevent mal-data and unauthorized  activities
  Scenario: As a system I want to reject failed login attempts
    Given The system is on login page
    When The system enters incorrect credentials
    When The system presses enter
    Then The system should see a message with the id=loginFailed

  Scenario: As a system I want to reject negative values for reimbursement amount so I can prevent mal-data
    Given The system is on submit page
    When The system enters negative amount and other fields
    When The system clicks submit
    Then The system should see a message with the id=fail

  Scenario: As a system I want to reject non-numeric values for reimbursement amount so I can prevent mal-data
    Given The system is on submit page
    When The system enters non-numeric amount and other fields
    When The system clicks submit
    Then The system should see a message with the id=fail
