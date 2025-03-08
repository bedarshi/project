import pandas as pd

# Correct file path (Use double backslashes or raw string)
file_path = r"C:\cognifilesinternship\level 1\task 1\Dataset .csv"

# Load the dataset
df = pd.read_csv(file_path)

# Identify restaurant chains (restaurants with multiple branches)
restaurant_counts = df["Restaurant Name"].value_counts()
restaurant_chains = restaurant_counts[restaurant_counts > 1]  # Restaurants appearing more than once

# Filter dataset to include only chain restaurants
chain_restaurants = df[df["Restaurant Name"].isin(restaurant_chains.index)]

# Analyze average ratings of restaurant chains
chain_avg_ratings = chain_restaurants.groupby("Restaurant Name")["Aggregate rating"].mean().sort_values(ascending=False)

# Analyze popularity of restaurant chains (total votes received)
chain_popularity = chain_restaurants.groupby("Restaurant Name")["Votes"].sum().sort_values(ascending=False)

# Display results
print("Top 5 Highest Rated Restaurant Chains:")
print(chain_avg_ratings.head(5))

print("\nTop 5 Most Popular Restaurant Chains (Based on Total Votes):")
print(chain_popularity.head(5))
