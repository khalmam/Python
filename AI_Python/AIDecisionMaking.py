from helper_functions import print_llm_response

task_list = [
    {
        "description": "Compose a brief email to my boss explaining that I will be late for next week's meeting.",
        "time_to_complete": 3
    },
    {
        "description": "Create an outline for a presentation on the benefits of remote work.",
        "time_to_complete": 60
    },
    {
        "description": "Write a 300-word review of the movie 'The Arrival'.",
        "time_to_complete": 30
    },
    {
        "description": "Create a shopping list for tofu and olive stir fry.",
        "time_to_complete": 5
    }
]

task = task_list[0]
print(task)

for task in task_list:
    if task["time_to_complete"] <= 5:
        task_to_do = task["description"]
        print_llm_response(task_to_do)        

for task in task_list:
    if task["time_to_complete"] <= 5:
        task_to_do = task["description"]
        print_llm_response(task_to_do) 
    else:
        print(f"To complete later: {task['time_to_complete']} time to complete.")


tasks_for_later = []

for task in task_list:
    if task["time_to_complete"] <= 5:
        task_to_do = task["description"]
        print_llm_response(task_to_do)
    else:
        tasks_for_later.append(task)

print(tasks_for_later)        