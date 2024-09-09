from helper_functions import print_llm_response, get_llm_response

ice_cream_flavors = [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip"
]

for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below, 
    provide a captivating description that could be used for promotional purposes.

    Flavor: {flavor}

    """
    print_llm_response(prompt)


    #saving results to a list
promotional_descriptions = []
for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below, 
    provide a captivating description that could be used for promotional purposes.

    Flavor: {flavor}

    """
    description = get_llm_response(prompt)
    promotional_descriptions.append(description)

    print(promotional_descriptions)