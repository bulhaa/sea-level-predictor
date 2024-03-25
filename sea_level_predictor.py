import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', )
    
    # Create scatter plot
    ax = df.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level', figsize=(6,6))

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = range(1880, 2051)
    plt.plot(x, res.intercept + res.slope * x, 'r', label='fitted line')
    
    # Create second line of best fit
    df_from_2000 = df.loc[df['Year'] >= 2000]
    res = linregress(df_from_2000['Year'], df_from_2000['CSIRO Adjusted Sea Level'])
    x = range(2000, 2051)
    plt.plot(x, res.intercept + res.slope * x, 'r', label='fitted line 2')
    plt.legend()
    
    # Add labels and title
    plt.title('Rise in Sea Level')
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()