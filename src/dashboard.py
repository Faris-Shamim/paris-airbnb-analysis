import streamlit as st
import matplotlib.pyplot as plt
import os
from analysis import *
from visuals import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("..")

st.set_page_config(page_title="Paris Airbnb Dashboard", layout="wide")
st.write("app loaded")
st.title("🗼 Paris Airbnb Dashboard")

# load and clean data
@st.cache_data
def get_data():
    df = load_data()
    df = clean_data(df)
    paris_df = get_paris_data(df)
    reviews_df = load_reviews()
    return paris_df, reviews_df

paris_df, reviews_df = get_data()

# analysis
neighbourhoods = neighbourhood_prices(paris_df)
most_expensive = neighbourhoods.idxmax()
accommodations = accommodations_analysis(paris_df, most_expensive)
over_time_data = over_time(paris_df)
reviews_over_time, reviews_by_neighbourhood, top_listings = reviews_analysis(reviews_df, paris_df)

# --- Section 1: Neighbourhood Prices ---
st.header("📍 Neighbourhood Prices")
fig, ax = plt.subplots(figsize=(10, 8))
neighbourhoods.plot(kind="barh", ax=ax, color="steelblue")
ax.set_title("Average Price by Neighbourhood", fontsize=14, fontweight="bold")
ax.set_xlabel("Average Price (€)")
st.pyplot(fig)

# --- Section 2: Accommodations ---
st.header("🏠 Accommodation Size vs Price")
neighbourhood_data, paris_data = accommodations
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
neighbourhood_data.plot(kind="barh", ax=axes[0], color="coral")
axes[0].set_title(f"Avg Price by Accommodation Size\n{most_expensive}", fontsize=13, fontweight="bold")
axes[0].set_xlabel("Average Price (€)")
paris_data.plot(kind="barh", ax=axes[1], color="steelblue")
axes[1].set_title("Avg Price by Accommodation Size\nAll of Paris", fontsize=13, fontweight="bold")
axes[1].set_xlabel("Average Price (€)")
plt.tight_layout()
st.pyplot(fig)

# --- Section 3: Trends Over Time ---
st.header("📈 Trends Over Time")
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(over_time_data["year"], over_time_data["new_hosts"], color="steelblue", marker="o", label="New Hosts")
ax1.set_xlabel("Year")
ax1.set_ylabel("New Hosts", color="steelblue")
ax1.tick_params(axis="y", labelcolor="steelblue")
ax2 = ax1.twinx()
ax2.plot(over_time_data["year"], over_time_data["avg_price"], color="coral", marker="s", label="Avg Price")
ax2.set_ylabel("Average Price (€)", color="coral")
ax2.tick_params(axis="y", labelcolor="coral")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.tight_layout()
st.pyplot(fig)

# --- Section 4: Reviews ---
st.header("⭐ Reviews Analysis")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(reviews_over_time["year"], reviews_over_time["review_count"], color="steelblue", marker="o")
    ax.set_title("Review Volume Over Time", fontsize=13, fontweight="bold")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Reviews")
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(8, 5))
    top_listings.plot(kind="barh", ax=ax, color="coral")
    ax.set_title("Top 10 Most Reviewed Listings", fontsize=13, fontweight="bold")
    ax.set_xlabel("Number of Reviews")
    plt.tight_layout()
    st.pyplot(fig)

fig, ax = plt.subplots(figsize=(10, 8))
reviews_by_neighbourhood.plot(kind="barh", ax=ax, color="steelblue")
ax.set_title("Review Count by Neighbourhood", fontsize=13, fontweight="bold")
ax.set_xlabel("Number of Reviews")
plt.tight_layout()
st.pyplot(fig)