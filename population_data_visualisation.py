import pandas as pd
import matplotlib.pyplot as plt
# I have done this in google colab
# 1: Load the dataset from the local file
# Use raw string literals to avoid Unicode escape issues
csv_file_path = r'/content/worldgrap.csv.csv'

# Load the CSV file
df = pd.read_csv(csv_file_path, skiprows=4)

# Inspect the dataframe
print(df.head())

# 2: Create a histogram for the total population in 2020
# Filter the data for the year 2020
df_2020 = df[['Country Name', '2020']].dropna()  # Remove rows with missing population data for 2020

# Plot a histogram
plt.figure(figsize=(10, 6), facecolor='black')  # Set the figure background to black
ax = plt.gca()
ax.set_facecolor('black')  # Set the background color of the plot area to black
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')

# Plot the histogram
plt.hist(df_2020['2020'], bins=30, edgecolor='black', color='white')  # White bars with black edges

# Customize the plot
plt.title('Distribution of Total Population in 2020', color='white')
plt.xlabel('Population', color='white')
plt.ylabel('Number of Countries', color='white')
plt.grid(True, color='gray')

# Customize tick parameters
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

plt.show()
