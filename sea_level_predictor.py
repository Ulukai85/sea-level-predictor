import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y)

    # Create first line of best fit
    res_1 = linregress(x, y)
    x_1 = range(min(x), 2051)
    plt.plot(x_1, res_1.intercept + res_1.slope * x_1, 'black', label='fitted line 1 (data: 1880-2013)')

    # Create second line of best fit
    df_2 = df[df['Year'] >= 2000]
    res_2 = linregress(df_2['Year'], df_2['CSIRO Adjusted Sea Level'])
    x_2 = range(2000, 2051)
    plt.plot(x_2, res_2.intercept + res_2.slope * x_2, 'r', label='fitted line 2 (data 2000-2013)')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()