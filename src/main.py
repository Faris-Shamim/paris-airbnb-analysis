from analysis import *
from visuals import *

def main():
    df = load_data()
    df = clean_data(df)

    paris_df = get_paris_data(df)

    # listings analysis
    neighbourhoods = neighbourhood_prices(paris_df)
    most_expensive = neighbourhoods.idxmax()
    accommodations = accommodations_analysis(paris_df, most_expensive)
    over_time_data = over_time(paris_df)

    # reviews analysis
    reviews_df = load_reviews()
    reviews_over_time, reviews_by_neighbourhood, top_listings = reviews_analysis(reviews_df, paris_df)

    # listings plots
    plot_neighbourhood_prices(neighbourhoods)
    plot_accommodations(accommodations, most_expensive)
    plot_over_time(over_time_data)

    # reviews plots
    plot_reviews_over_time(reviews_over_time)
    plot_reviews_by_neighbourhood(reviews_by_neighbourhood)
    plot_top_listings(top_listings)

if __name__ == "__main__":
    main()