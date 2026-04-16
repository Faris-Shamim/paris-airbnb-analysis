import matplotlib.pyplot as plt

def plot_neighbourhood_prices(data):
    fig, ax = plt.subplots(figsize=(10, 8))
    data.plot(kind="barh", ax=ax, color="steelblue")
    ax.set_title("Average Price by Neighbourhood", fontsize=14, fontweight="bold")
    ax.set_xlabel("Average Price (€)")
    ax.set_ylabel("Neighbourhood")
    plt.tight_layout()
    plt.show()

def plot_accommodations(data, name):
    neighbourhood_data, paris_data = data
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    neighbourhood_data.plot(kind="barh", ax=axes[0], color="coral")
    axes[0].set_title(f"Avg Price by Accommodation Size\n{name}", fontsize=13, fontweight="bold")
    axes[0].set_xlabel("Average Price (€)")
    axes[0].set_ylabel("Accommodates (persons)")

    paris_data.plot(kind="barh", ax=axes[1], color="steelblue")
    axes[1].set_title("Avg Price by Accommodation Size\nAll of Paris", fontsize=13, fontweight="bold")
    axes[1].set_xlabel("Average Price (€)")
    axes[1].set_ylabel("")

    plt.tight_layout()
    plt.show()

def plot_over_time(data):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.plot(data["year"], data["new_hosts"], color="steelblue", marker="o", label="New Hosts")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("New Hosts", color="steelblue")
    ax1.tick_params(axis="y", labelcolor="steelblue")

    ax2 = ax1.twinx()
    ax2.plot(data["year"], data["avg_price"], color="coral", marker="s", label="Avg Price")
    ax2.set_ylabel("Average Price (€)", color="coral")
    ax2.tick_params(axis="y", labelcolor="coral")

    fig.suptitle("New Hosts & Average Price Over Time", fontsize=14, fontweight="bold")
    fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
    plt.tight_layout()
    plt.show()

def plot_reviews_over_time(reviews_over_time):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(reviews_over_time["year"], reviews_over_time["review_count"], color="steelblue", marker="o")
    ax.set_title("Review Volume Over Time", fontsize=14, fontweight="bold")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Reviews")
    plt.tight_layout()
    plt.show()

def plot_reviews_by_neighbourhood(reviews_by_neighbourhood):
    fig, ax = plt.subplots(figsize=(10, 8))
    reviews_by_neighbourhood.plot(kind="barh", ax=ax, color="steelblue")
    ax.set_title("Review Count by Neighbourhood", fontsize=14, fontweight="bold")
    ax.set_xlabel("Number of Reviews")
    ax.set_ylabel("Neighbourhood")
    plt.tight_layout()
    plt.show()

def plot_top_listings(top_listings):
    fig, ax = plt.subplots(figsize=(8, 6))
    top_listings.plot(kind="barh", ax=ax, color="coral")
    ax.set_title("Top 10 Most Reviewed Listings", fontsize=14, fontweight="bold")
    ax.set_xlabel("Number of Reviews")
    ax.set_ylabel("Listing ID")
    plt.tight_layout()
    plt.show()