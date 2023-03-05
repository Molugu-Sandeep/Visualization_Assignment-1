import pandas as pd
import matplotlib.pyplot as plt


# Reading The CSV file to a Pandas DataFrame

df = pd.read_csv('Country_GDP_Data.csv')

"""
This DataFrame contains GDP data for multiple countries and years. The columns are as follows:

- 'Country Name': the name of each country
- '2012'-'2021': the GDP for each country in each year
- 'Total GDP': the total GDP for each country from 2012-2021

"""


#Sort the DataFrame in descending order based on the 'Total GDP' column and Select the top 6 countries based on their 'Total GDP'


df_sorted = df.sort_values(by=['Total GDP'], ascending=False)

"""
This code creates a new DataFrame containing only the top 6 countries by total GDP. This is necessary because we want to focus our analysis on the countries with the largest economies, and the full dataset contains many countries that are not relevant to our analysis.

"""

top_6_countries = df_sorted.iloc[:6, :]


# The Top 6 Countries
top_6_countries


# Defining the Three functions that will create the visualizations
def line_plot():
    # Set the x and y axis values
    x = top_6_countries.columns[3:13]
    y = top_6_countries.iloc[:, 3:13].T.values

    # Create the line plot
    plt.figure(figsize=(10, 6))
    for i in range(len(top_6_countries)):
        plt.plot(x, y[:, i], label=top_6_countries.iloc[i]['Country Name'])
    plt.xlabel('Year')
    plt.ylabel('GDP')
    plt.title('GDP of Top 6 Countries')
    plt.legend()
    plt.show()

    """
    Plots a line chart showing the GDP of the top 6 countries over time.

    Parameters:
    df (pandas.DataFrame): a dataframe containing the GDP data for multiple countries and years.

    Returns:
    None
    """
    
    
# Define a function to create a bar chart of the Total GDP of the top 6 countries
def bar_chart():
    # Set the x and y axis values
    x = top_6_countries['Country Name']
    y = top_6_countries['Total GDP']

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(x, y)
    plt.xlabel('Country')
    plt.ylabel('Total GDP')
    plt.title('Total GDP of Top 6 Countries')
    plt.show()

# Define a function to create a scatter plot of the GDP of the top 6 countries in 2021
def scatter_plot():
    # Set the x and y axis values
    x = top_6_countries['Country Name']
    y = top_6_countries['2021']

    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y)
    plt.xlabel('Country')
    plt.ylabel('GDP in 2021')
    plt.title('GDP of Top 6 Countries in 2021')
    plt.show()


# Calling The Functions To Create The Visualizations
# 1. The Line Chart
line_plot()

# 2. The Bar Chart
bar_chart()

# 3. The Scatter Plot
scatter_plot()

