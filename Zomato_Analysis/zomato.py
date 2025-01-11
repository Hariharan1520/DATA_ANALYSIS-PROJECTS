import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from a CSV file into a DataFrame
dataframe = pd.read_csv('Zomato data.csv')

# Display the first five rows of the dataset for a quick preview of its structure
print(dataframe.head())

# Define a function to handle and process the 'rate' column
def handleRate(value):
    # Split the rate value on '/' and take the first part (actual rating)
    value = str(value).split('/')
    value = value[0]
    # Convert the rating to a float and return
    return float(value)

# Apply the handleRate function to the 'rate' column to clean and standardize it
dataframe['rate'] = dataframe['rate'].apply(handleRate)
# Display the updated DataFrame to verify the changes
print(dataframe.head())

# Visualize the count of different types of restaurants
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")  # Set the x-axis label
plt.show()

# Group the data by 'listed_in(type)' and sum the 'votes' for each group
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
# Create a DataFrame to store the grouped data
result = pd.DataFrame({'votes': grouped_data})
# Plot the grouped data as a line plot
plt.plot(result, c="blue", marker="o")
plt.xlabel("Type of restaurant", c="red", size=10)  # Customize x-axis label
plt.ylabel("Votes", c="red", size=10)  # Customize y-axis label
plt.show()

# Find the maximum number of votes
max_votes = dataframe['votes'].max()
# Identify the restaurant(s) with the maximum votes
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
print("Restaurant(s) with max votes", '\n', restaurant_with_max_votes)

# Visualize the distribution of online order availability
sns.countplot(x=dataframe['online_order'])
plt.title("Online Order Availability")
plt.show()

# Plot a histogram to visualize the distribution of restaurant ratings
plt.hist(dataframe['rate'], bins=5)
plt.title("Rating Distribution")
plt.xlabel("Ratings")
plt.ylabel("Frequency")
plt.show()

# Extract the 'approx_cost(for two people)' column to analyze
couple_data = dataframe['approx_cost(for two people)']
# Visualize the distribution of approximate cost for two people
sns.countplot(x=couple_data)
plt.title("Approximate Cost for Two People")
plt.show()

# Create a boxplot to analyze the relationship between 'online_order' and 'rate'
plt.figure(figsize=(6, 6))  # Set the figure size
sns.boxplot(x='online_order', y='rate', data=dataframe)
plt.title("Online Order vs. Rating")
plt.xlabel("Online Order")
plt.ylabel("Rating")
plt.show()

# Create a pivot table to count occurrences of 'online_order' across different restaurant types
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
# Visualize the pivot table as a heatmap
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap of Online Order vs. Restaurant Type")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()
