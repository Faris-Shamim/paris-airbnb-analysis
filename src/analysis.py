import pandas as pd

def load_data():
    try:
        df = pd.read_csv("data/listings_small.csv", encoding="ISO-8859-1", low_memory=False)
        return df
    except FileNotFoundError:
        raise FileNotFoundError("Could not find 'data/Listings.csv'. Check your file path.")

def load_reviews():
    try:
        df = pd.read_csv("data/reviews_small.csv", encoding="ISO-8859-1", low_memory=False)
        return df
    except FileNotFoundError:
        raise FileNotFoundError("Could not find 'data/Reviews.csv'. Check your file path.")
    
def clean_data(df):
    df = df.copy()  # avoid modifying the original dataframe
    df["host_since"] = pd.to_datetime(df["host_since"], errors="coerce")
    df["price"] = df["price"].replace("[$,]", "", regex=True).astype(float)
    df = df.dropna(subset=["price", "neighbourhood", "host_since"])  # drop rows missing key data
    return df

def get_paris_data(df):
    paris_df = df[df["city"] == "Paris"][[
        "listing_id", "host_since", "neighbourhood", "city", "accommodates", "price"
    ]]
    if paris_df.empty:
        raise ValueError("No Paris data found. Check the 'city' column values.")
    return paris_df

def neighbourhood_prices(paris_df):
    return paris_df.groupby("neighbourhood")["price"].mean().sort_values()

def accommodations_analysis(paris_df, neighbourhood):
    neighbourhood_data = (
        paris_df[paris_df["neighbourhood"] == neighbourhood]
        .groupby("accommodates")["price"]
        .mean()
        .sort_values()
    )
    paris_data = (
        paris_df.groupby("accommodates")["price"]
        .mean()
        .sort_values()
    )
    return neighbourhood_data, paris_data

def over_time(paris_df):
    df = paris_df.copy()
    df["year"] = df["host_since"].dt.year
    return df.groupby("year").agg(
        avg_price=("price", "mean"),
        new_hosts=("host_since", "count")
    ).reset_index()

def reviews_analysis(reviews_df, paris_df):
    merged = reviews_df.merge(paris_df[["listing_id", "neighbourhood"]], on="listing_id", how="inner")
    
    merged["date"] = pd.to_datetime(merged["date"], errors="coerce")
    merged["year"] = merged["date"].dt.year
    
    reviews_over_time = merged.groupby("year")["review_id"].count().reset_index()
    reviews_over_time.columns = ["year", "review_count"]
    
    reviews_by_neighbourhood = merged.groupby("neighbourhood")["review_id"].count().sort_values()
    
    top_listings = merged.groupby("listing_id")["review_id"].count().sort_values(ascending=False).head(10)
    
    return reviews_over_time, reviews_by_neighbourhood, top_listings