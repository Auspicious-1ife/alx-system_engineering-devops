#!/usr/bin/python3
"""
Script to gather TODO list progress for a given employee ID using a REST API and
export the data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_name = user.get('name')
    username = user.get('username')

    # Fetch TODO list for the user
    todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()

    # Calculate progress
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get('completed')]
    num_completed_tasks = len(completed_tasks)

    # Display result
    print(
        f"Employee {employee_name} is done with tasks("
        f"{num_completed_tasks}/{total_tasks}):"
    )
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))

    # Prepare data for JSON export
    tasks_list = []
    for task in todos:
        tasks_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    # Export data to JSON
    json_data = {str(employee_id): tasks_list}
    with open(f"{employee_id}.json", mode='w') as file:
        json.dump(json_data, file)
