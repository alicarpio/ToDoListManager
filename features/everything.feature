Feature: To-Do List Manager

  Scenario: Adding a task
    Given the To-Do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: Listing all tasks
    Given the To-Do list is empty
    And the user adds a task "Buy groceries"
    And the user adds a task "Walk the dog"
    When the user lists all tasks
    Then the to-do list should contain "Buy groceries"
    And the to-do list should contain "Walk the dog"

  Scenario: Marking a task as completed
    Given the To-Do list is empty
    And the user adds a task "Buy groceries"
    When the user marks the task with ID 1 as completed
    Then the task with ID 1 should be marked as completed

  Scenario: Clearing the entire to-do list
    Given the To-Do list is empty
    And the user adds a task "Buy groceries"
    And the user adds a task "Walk the dog"
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Setting a category for a task
    Given the To-Do list is empty
    And the user adds a task "Buy groceries"
    When the user sets the category "Shopping" for the task with ID 1
    Then the task with ID 1 should have the category "Shopping"

  Scenario: Marking a non-existent task as completed
    Given the To-Do list is empty
    When the user marks the task with ID 1 as completed
    Then an error message "Task with ID 1 not found." should be shown
