import pandas as pd

df = pd.read_csv("data/listings.csv", encoding="ISO-8859-1")

df_small = df.sample(n=5000, random_state=42)
df_small.to_csv("data/listings_small.csv", index=False)

# reviews
reviews = pd.read_csv("data/reviews.csv", encoding="ISO-8859-1")
reviews_small = reviews.sample(n=5000, random_state=42)
reviews_small.to_csv("data/reviews_small.csv", index=False)

print("Small datasets created!")

