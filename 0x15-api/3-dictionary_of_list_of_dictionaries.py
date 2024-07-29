#!/usr/bin/python3
"""
Script to gather TODO list progress for all
employees using a REST API and
export the data in the JSON format.
"""

import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users = requests.get(f"{base_url}/users").json()

    all_tasks = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        # Fetch TODO list for each user
        todos = requests.get(f"{base_url}/todos?userId={user_id}").json()

        tasks_list = []
        for task in todos:
            tasks_list.append({
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            })

        # Store tasks in the dictionary with user_id as the key
        all_tasks[user_id] = tasks_list

    # Export data to JSON
    with open("todo_all_employees.json", mode='w') as file:
        json.dump(all_tasks, file)
