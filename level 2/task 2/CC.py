import pandas as pd

# Correct file path (Use double backslashes or raw string)
file_path = r"C:\cognifilesinternship\level 1\task 1\Dataset .csv"

# Load the dataset
df = pd.read_csv(file_path)

# Identify the most common cuisine combinations
cuisine_combinations_counts = df["Cuisines"].value_counts()

# Get the top 5 most common cuisine combinations
top_cuisine_combinations = cuisine_combinations_counts.head(5)

# Calculate the average rating for each cuisine combination
cuisine_avg_ratings = df.groupby("Cuisines")["Aggregate rating"].mean()

# Get the top 5 highest-rated cuisine combinations
top_rated_cuisine_combinations = cuisine_avg_ratings.sort_values(ascending=False).head(5)

# Display results
print("Most Common Cuisine Combinations:")
print(top_cuisine_combinations)

print("\nTop Rated Cuisine Combinations:")
print(top_rated_cuisine_combinations)
