#!/usr/bin/python3
"""Script uses REST API
To derive the information about all employee's TODO list progress
The information should be exported in JSON format
"""
import json
import requests


def get_employee_todo_progress():
    """Prints the employees' TODO list progress
    Returns:
    int: the user_id
    str: task completed status
    str: the task's title
    str: username
    """
    users_url = f"https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        print("User not found")
        return

    user_data = users_response.json()

    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos"
    )
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("TODO list not found")
        return

    todos_data = todos_response.json()
    all_data = {}
    for user in user_data:
        user_id = str(user["id"])
        username = user["username"]
        all_data[user_id] = []

        for task in todos_data:
            if task["userId"] == user["id"]:
                all_data[user_id].append({
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                })

    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(all_data, json_file)


if __name__ == "__main__":
    get_employee_todo_progress()
