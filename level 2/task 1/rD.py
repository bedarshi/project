import pandas as pd
import matplotlib.pyplot as plt

# Correct file path (Use double backslashes or raw string)
file_path = r"C:\cognifilesinternship\level 1\task 1\Dataset .csv"

# Load the dataset
df = pd.read_csv(file_path)

# Analyze the distribution of aggregate ratings
rating_counts = df["Aggregate rating"].value_counts().sort_index()

# Determine the most common rating range
most_common_rating = rating_counts.idxmax()
most_common_rating_count = rating_counts.max()

# Calculate the average number of votes received by restaurants
average_votes = df["Votes"].mean()

# Plot the distribution of ratings
plt.figure(figsize=(8, 5))
plt.bar(rating_counts.index, rating_counts.values, color='lightcoral', edgecolor='black')
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Aggregate Ratings Among Restaurants")
plt.xticks(rating_counts.index, rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Display results
print("Most Common Rating:", most_common_rating, "(Count:", most_common_rating_count, ")")
print("Average Votes per Restaurant:", round(average_votes, 2))
