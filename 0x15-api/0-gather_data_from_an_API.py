#!/usr/bin/python3
"""Script uses REST API
Returns information about employee's TODO list progress
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Prints the employee's TODO list progress
    Parameters:
    int: The employee Id
    Returns:
    str: employee's name
    int: number of completed tasks
    int: total number of tasks
    str: the task's title
    """
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print("User not found")
        return

    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    todos_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    )
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("TODO list not found")
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]

    number_of_done_tasks = len(done_tasks)

    print(
        f"Employee {employee_name} is done with tasks("
        f"{number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("The employee ID must be an integer")
        sys.exit(1)
