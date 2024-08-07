#!/usr/bin/python3
"""Script uses REST API
To derive the information about employee's TODO list progress
The information should be exported in csv format
"""
import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Prints the employee's TODO list progress
    Parameters:
    int: The employee Id
    Returns:
    int: the employee_id
    str: employee's name
    str: task completed status
    str: the task's title
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

    csv_filename = f"{user_id}.csv"
    with open(
            csv_filename, mode='w', newline='', encoding='utf-8'
            ) as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow(
                    [user_id, user_name, str(
                        task.get("completed")
                        ), task.get("title")]
                    )


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("The employee ID must be an integer")
        sys.exit(1)
