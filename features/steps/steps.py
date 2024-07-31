from behave import given, when, then
from main import ToDoListManager

@given('the To-Do list is empty')
def step_given_todo_list_is_empty(context):
    context.manager = ToDoListManager()

@when('the user adds a task "{description}"')
def step_when_user_adds_task(context, description):
    context.manager.add_task(description)

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    context.tasks = context.manager.tasks

@then('the to-do list should contain "{description}"')
def step_then_todo_list_should_contain(context, description):
    tasks_descriptions = [task.description for task in context.manager.tasks]
    assert description in tasks_descriptions, f'Task "{description}" not found in the to-do list'

@when('the user marks the task with ID {task_id:d} as completed')
def step_when_user_marks_task_completed(context, task_id):
    context.manager.mark_task_as_completed(task_id)

@then('the task with ID {task_id:d} should be marked as completed')
def step_then_task_should_be_completed(context, task_id):
    task = next((task for task in context.manager.tasks if task.task_id == task_id), None)
    assert task is not None, f'Task with ID {task_id} not found'
    assert task.completed, f'Task with ID {task_id} is not marked as completed'

@when('the user clears the to-do list')
def step_when_user_clears_todo_list(context):
    context.manager.clear_tasks()

@then('the to-do list should be empty')
def step_then_todo_list_should_be_empty(context):
    assert len(context.manager.tasks) == 0, 'The to-do list is not empty'

@when('the user sets the category "{category}" for the task with ID {task_id:d}')
def step_when_user_sets_category(context, category, task_id):
    context.manager.set_task_category(task_id, category)

@then('the task with ID {task_id:d} should have the category "{category}"')
def step_then_task_should_have_category(context, task_id, category):
    task = next((task for task in context.manager.tasks if task.task_id == task_id), None)
