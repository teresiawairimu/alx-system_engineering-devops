#!/usr/bin/python3
"""Script uses REST API
To derive the information about employee's TODO list progress
The information should be exported in JSON format
"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Prints the employee's TODO list progress
    Parameters:
    int: The employee Id
    Returns:
    int: the user_id
    str: task completed status
    str: the task's title
    str: username
    """
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print("User not found")
        return

    user_data = employee_response.json()
    user_name = user_data.get("username")
    user_id = user_data.get("id")

    todos_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    )
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("TODO list not found")
        return

    todos_data = todos_response.json()
    json_data = {
        str(user_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_name
            }
            for task in todos_data
        ]
    }
    json_filename = f"{user_id}.json"
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("The employee ID must be an integer")
        sys.exit(1)
