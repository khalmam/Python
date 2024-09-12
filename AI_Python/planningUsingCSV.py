# Imports
from helper_functions import get_llm_response, print_llm_response, display_table
from IPython.display import Markdown
import csv

f = open("itinerary.csv", 'r')

csv_reader = csv.DictReader(f)
itinerary = []
for row in csv_reader:
    print(row)
    itinerary.append(row)
f.close()

print(itinerary)

# Create an empty list to store the filtered data
filtered_data = []

# Filter by country
for trip_stop in itinerary:
    # For example: get the destinations located in "Japan"
    if trip_stop["Country"] == "Japan":
        filtered_data.append(trip_stop)

# Select the first destination from the itinerary list (Hint: index=0)
trip_stop = itinerary[0]
print(trip_stop)

city = trip_stop["City"]
country = trip_stop["Country"]
arrival = trip_stop["Arrival"]
departure = trip_stop["Departure"]

prompt = f"""I will visit {city}, {country}, from {arrival} to {departure}. 
Please create a detailed daily itinerary."""

print(prompt)

# Store the LLM response
response = get_llm_response(prompt)

# Print in Markdown format
display(Markdown(response))



#Exercise 1

# Create an empty list to store the filtered data
filtered_data = []

# Filter by country
for trip_stop in itinerary:
    # For example: get the destinations located in "Brazil"
    # Complete code on next line:
    if trip_stop["Country"] == "Brazil":
        filtered_data.append(trip_stop)

print(filtered_data)


trip_stop = itinerary[0]

city = trip_stop["City"]
country = trip_stop["Country"]
arrival = trip_stop["Arrival"]
departure = trip_stop["Departure"]

print(f" The city is: {city}")
print(f" The country is: {country}")
print(f" The arrival date is: {arrival}")
print(f" The departure date is: {departure}")


#Challenge exercise!
#omplete the code below so that it will print out the country of every destination in the itinerary.csv file. Ask the chatbot for help if you need it!

f = open("itinerary.csv", "r")
csv_reader = csv.DictReader(f)
itinerary = []
for row in csv_reader:
    itinerary.append(row)
f.close()

# Complete the next two lines to print the country:
for trip_stop in itinerary :
    print(trip_stop['Country'])