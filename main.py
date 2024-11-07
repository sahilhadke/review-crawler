# main.py
from reviewcrawler import GoogleCrawler, YelpCrawler

def main():
    
    
    # Dynamic input for crawler type, max reviews, restaurant name, and location
    crawler_type = "both"
    max_reviews = 25
    restaurant_name = "The Chuckbox"
    location = "Tempe"
    min_sleep_time = 3
    max_sleep_time = 4

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
        print("Unsupported crawler type.")
        return

    # Run the crawler
    if gcrawler:
        gcrawler.crawl()
    if ycrawler:
        ycrawler.crawl()

if __name__ == "__main__":
    main()