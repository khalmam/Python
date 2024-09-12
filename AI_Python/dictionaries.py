from helper_functions import print_llm_response, get_llm_response

ice_cream_flavors = {
    "Mint Chocolate Chip": "Refreshing mint ice cream studded with decadent chocolate chips.",
    "Cookie Dough": "Vanilla ice cream loaded with chunks of chocolate chip cookie dough.",
    "Salted Caramel": "Sweet and salty with a smooth caramel swirl and a hint of sea salt."}

print(ice_cream_flavors.keys())

print(ice_cream_flavors.values())

#Acccesing elements
cookie_dough_description = ice_cream_flavors["Cookie Dough"]
print(cookie_dough_description)

#Adding Elements
ice_cream_flavors["Rocky Road"] = "Chocolate ice cream mixd witother ngredients."

#Updating existing elements
ice_cream_flavors["Rocky Road"] = "Chocolate ice cream mixed with other ingredients."


isabel_facts = {
    "age": 28,
    "Favorite color": "red"
}
print(isabel_facts)

#You can store information within that dictionary using lists. For instance, the names for each of her cats.
isabel_facts["Cat names"] = ["Charlie", "Smokey", "Tabitha"]

#or something else
isabel_facts["Cat names"] = ["Charlie", "Smokey", "Tabitha"]

#Using dictionaries to complete high priority tasks using AI


#instead of that unorganized large list, divide tasks by priority
high_priority_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Create an outline for a presentation on the benefits of remote work."
]

medium_priority_tasks = [
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Draft a thank-you note for my neighbor Dapinder who helped water my plants while I was on vacation."
]

low_priority_tasks = [
    "Write a 300-word review of the movie 'The Arrival'."
]

#create dictionary with all tasks
#dictionaries can contain lists!
prioritized_tasks = {
    "high_priority": high_priority_tasks,
    "medium_priority": medium_priority_tasks,
    "low_priority": low_priority_tasks
}

#complete high priority tasks 
for task in prioritized_tasks["high_priority"]:
    print_llm_response(task)
