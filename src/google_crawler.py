import os
from .base_crawler import ReviewCrawler

class GoogleReviewCrawler(ReviewCrawler):
    def crawl(self):
        
        print(self.config)
    
        reviews = []

        # Save reviews to JSON
        self.save_reviews(reviews, "google")
