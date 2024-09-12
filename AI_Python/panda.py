# Lesson 3: Using third-party packages

#In this lesson, you'll try out some third-party Python packages that let you explore and visualize data!

## Loading and exploring data with ```pandas```

#One of the most popular Python third-party packages is called ```pandas```. 

#It helps you with loading and exploring structured data, like the kind stored in spreadsheets and ```.csv``` files. Check out the [Pandas documentation](https://pandas.pydata.org/) if you want to learn more!

#To use the ```pandas``` package, you first need to load it:

import pandas as pd


#So `import pandas as pd` creates a shortcut that you can use to avoid typing pandas. 

#**Note:** you'll need to use the `.` notation when using the function in pandas - go back to the "Using functions from a local file" lesson in this course if you need a refresher!

#Next, you'll load a CSV file of used car sales prices using pandas:

# Dataset adapted from here https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho
data = pd.read_csv('car_data.csv')

print(data)

#How do you show only cars that sold for more than $10,000? Let's ask the chatbot!



#Next, run the code the LLM wrote to filter the data by price:

# Code to show only the cars with a price >= 10000
print(data[data["Price"]>=10000])

#You can also filter by other columns in the data, for example the year:

# Show all the cars from the 2015 
print(data[data["Year"]==2015])

#Pandas includes built-in tools to calculate interesting statistics, like the median selling value for the cars from 2015. Here's the code:

filtered_data = data[data["Year"]==2015]
print(filtered_data["Price"].median())

## Plotting data with ```matplotlib```

#This is a popular package used by data scientists and developers to visualize data. You can check out the [Matplotlib documentation](https://matplotlib.org/) if you want to learn more!

#To use matplotlib, you first have to import it with the following command:

# Note the .pyplot
import matplotlib.pyplot as plt

#Don't worry about remembering this command, you can always find it by asking a chatbot or searching online. Again, the `as` form of the import command is being used to set up an alias - so now you can type `plt` instead of `matplotlib.pyplot` saving you lots of typing!

#Let's start by using ```matplotlib.pyplot``` to plot the selling price of a car against how many miles it has driven:

plt.scatter(data["Kilometer"], data["Price"])

plt.title('Car Price vs. Kilometers Driven')
plt.xlabel('Kilometers Driven')
plt.ylabel('Price (in USD)')

plt.show()

#Matplotlib has many settings that can help you customize your charts. You can ask a chatbot to help you write the code to modify these settings:


#Let's try the code the chatbot suggested:

plt.scatter(data["Kilometer"], data["Price"], color='gold')
plt.title('Car Price vs. Kilometers Driven', fontsize=16)
plt.xlabel('Kilometers Driven')
plt.ylabel('Price (in USD)')

# Add the grid
plt.grid(True)

# Display the plot
plt.show()

## Extra practice

U#se the 🤖 chatbot to help you try the following exercises!

### Exercise 1

#Write code to create a filtered table of all the Honda Accords in the dataset.

#**Hint:** You can always copy and paste the code from the earlier parts of this notebook and ask the chatbot to modify it!

import pandas as pd

# Load your CSV file into a DataFrame
data = pd.read_csv('car_data.csv')

honda_accords = data[data["Model"] == "Accord"]
print(honda_accords)

### Exercise 2

#Write code to display a scatter plot of sales price vs year.

# WRITE YOUR CODE HERE
import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file into a DataFrame
data = pd.read_csv('car_data.csv')

# Create a scatter plot of sales price vs year
plt.scatter(data['Year'], data['Price'])
plt.xlabel('Year')
plt.ylabel('Price')
plt.title('Scatter Plot of Sales Price vs Year')
plt.show()

### Challenge exercise!

#Ask the LLM to help you create a pie chart of the data showing how many cars were sold each year.

#**Hint:** Be sure you tell the chatbot what your data variable is called! It may pick a different name by default.

# WRITE YOUR CODE HERE
import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file into a DataFrame
data = pd.read_csv('car_data.csv')

# Assume there's a column 'Year' and we count the occurrences of each year
sales_per_year = data['Year'].value_counts()

# Create a pie chart of the number of cars sold each year
plt.pie(sales_per_year, labels=sales_per_year.index, autopct='%1.1f%%', startangle=140)
plt.title('Cars Sold Each Year')
plt.show()