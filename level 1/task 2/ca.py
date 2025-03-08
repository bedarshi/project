import pandas as pd

# Correct file path (Use double backslashes or raw string)
file_path = r"C:\cognifilesinternship\level 1\task 1\Dataset .csv"

# Load the dataset
df = pd.read_csv(file_path)

# Identify the city with the highest number of restaurants
city_counts = df["City"].value_counts()
top_city = city_counts.idxmax()
top_city_count = city_counts.max()

# Calculate the average rating for each city
city_avg_rating = df.groupby("City")["Aggregate rating"].mean()

# Identify the city with the highest average rating
top_rated_city = city_avg_rating.idxmax()
top_rated_city_avg = city_avg_rating.max()

# Display results
print("City with the Most Restaurants:", top_city, "(", top_city_count, "restaurants )")
print("City with the Highest Average Rating:", top_rated_city, "( Average rating:", round(top_rated_city_avg, 2), ")")
