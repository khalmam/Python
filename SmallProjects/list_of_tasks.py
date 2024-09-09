from helper_functions import print_llm_response, get_llm_response

list_of_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Write a 300-word review of the movie 'The Arrival'."
]
for task in list_of_tasks:
    print(task)

for task in list_of_tasks:
    print_llm_response(task)

    