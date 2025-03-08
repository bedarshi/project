import pandas as pd
import matplotlib.pyplot as plt

# Correct file path (Use double backslashes or raw string)
file_path = r"C:\cognifilesinternship\level 1\task 1\Dataset .csv"

# Load the dataset
df = pd.read_csv(file_path)

# Count occurrences of each price range
price_range_counts = df["Price range"].value_counts().sort_index()

# Calculate the percentage of restaurants in each price range
price_range_percentage = (price_range_counts / len(df)) * 100

# Plot the bar chart
plt.figure(figsize=(8, 5))
plt.bar(price_range_counts.index, price_range_counts.values, color='skyblue', edgecolor='black')
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Price Ranges Among Restaurants")
plt.xticks(price_range_counts.index)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Display percentage distribution
print("Percentage of restaurants in each price range:")
print(price_range_percentage)
