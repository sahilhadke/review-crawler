# test_review_crawler.py
import pytest
from reviewcrawler import GoogleCrawler, YelpCrawler

@pytest.mark.parametrize("crawler_type, max_reviews, restaurant_name, location", [
    ("google", 10, "The Best Restaurant", "New York"),
    ("yelp", 5, "Top Cafe", "San Francisco")
])
def test_review_crawler(crawler_type, max_reviews, restaurant_name, location):
    if crawler_type == "google":
        crawler = GoogleCrawler()
        crawler.setUp()  # Initialize SeleniumBase
        crawler.crawl(max_reviews, restaurant_name, location)
        crawler.tearDown()  # Clean up SeleniumBase
    elif crawler_type == "yelp":
        crawler = YelpCrawler()
        crawler.setUp()  # Initialize SeleniumBase
        crawler.crawl(max_reviews, restaurant_name, location)
        crawler.tearDown()  # Clean up SeleniumBase
