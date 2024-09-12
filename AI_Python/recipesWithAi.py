from helper_functions import print_llm_response, get_llm_response

food_preferences_tommy = {
        "dietary_restrictions": "vegetarian",
        "favorite_ingredients": ["tofu", "olives"],
        "experience_level": "intermediate",
        "maximum_spice_level": 6,
        "favorite_cuisine": "Japanese",
}

available_spices = ["cumin", "turmeric", "oregano", "paprika"]

prompt = f"""Please suggest a recipe that tries to include 
the following ingredients: 
{food_preferences_tommy["favorite_ingredients"]}.
The recipe should adhere to the following dietary restrictions:
{food_preferences_tommy["dietary_restrictions"]}.
The difficulty of the recipe should be: 
{food_preferences_tommy["experience_level"]}
The maximum spice level on a scale of 10 should be: 
{food_preferences_tommy["maximum_spice_level"]} 
The cuisine should be:
{food_preferences_tommy["favorite_cuisine"]} 
Provide a two sentence description.

The recipe should not include spices outside of this list:
Spices: {available_spices}
"""

recipe = get_llm_response(prompt)

print(recipe)

