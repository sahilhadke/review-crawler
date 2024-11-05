from src.yelp_crawler import YelpReviewCrawler
from src.google_crawler import GoogleReviewCrawler

def main(platform, restaurant_name):
    
    # Select crawler based on platform
    if platform.lower() == "yelp":

        crawler = YelpReviewCrawler(restaurant_name)
        crawler.crawl()

    elif platform.lower() == "google":

        crawler = GoogleReviewCrawler(restaurant_name)
        crawler.crawl()
        
    elif platform.lower() == "all":
        
        crawler = YelpReviewCrawler(restaurant_name)
        crawler.crawl()

        crawler = GoogleReviewCrawler(restaurant_name)
        crawler.crawl()

    else:
        raise ValueError("Unsupported platform. Choose 'yelp' or 'google'.")
    

if __name__ == "__main__":
    main("google", "mcdonalds")