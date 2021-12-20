Feature: Manager should be able to manage reimbursements
  Scenario: As a manager I want to view pending reimbursement requests so I can manage them
    Given The manager is on manager home page or past page
    When The manager is clicks pending page
    Then The manager should be redirected to the manager pending page with the title Manager Pending Page

  Scenario: Scenario: As a manager I want to approve reimbursement requests and leave a comment so I can compensate the employee for legitimate cause
    Given The manager is on manager pending page
    When The manager enters comment for approval
    When The manager clicks approve button
    Then The manager will see a message

  Scenario: Scenario: As a manager I want to reject reimbursement requests and leave a comment so I can reject employee's illegitimate request
    Given The manager is on manager pending page
    When The manager enters comment for rejection
    When The manager clicks reject button
    Then The manager will see a message
