# main.py
from reviewcrawler import GoogleCrawler, YelpCrawler

def main():
    """
    Main function to run the review crawlers.
    """

    # Get dynamic input for crawler type, max reviews, restaurant name, and location
    crawler_type = "both"   # "google", "yelp", or "both"
    max_reviews = 2  # Maximum number of reviews to crawl
    restaurant_name = "The Dhaba"  # Name of the restaurant to crawl
    location = "Tempe"  # Location of the restaurant
    min_sleep_time = 3  # Minimum time to sleep between requests in seconds
    max_sleep_time = 4  # Maximum time to sleep between requests in seconds

    # Instantiate the appropriate crawler
    gcrawler = None
    ycrawler = None
    if crawler_type == "google":
        gcrawler = GoogleCrawler(max_reviews, restaurant_name, location, (min_sleep_time, max_sleep_time))
    elif crawler_type == "yelp":
        ycrawler = YelpCrawler(max_reviews, restaurant_name, location, (min_sleep_time, max_sleep_time))
    elif crawler_type == "both":
        gcrawler = GoogleCrawler(max_reviews, restaurant_name, location, (min_sleep_time, max_sleep_time))
        ycrawler = YelpCrawler(max_reviews, restaurant_name, location, (min_sleep_time, max_sleep_time))
    else:
        return

    # Run the crawler
    if gcrawler:
        gcrawler.crawl()
    if ycrawler:
        ycrawler.crawl()

if __name__ == "__main__":
    main()

