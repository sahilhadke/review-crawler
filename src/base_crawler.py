import json
import os
from seleniumbase import BaseCase
import src.config as config

class ReviewCrawler(BaseCase):
    
    def __init__(self, restaurant_name, output_path="output"):
        super().__init__()
        self.restaurant_name = restaurant_name
        self.output_path = output_path
        self.config = config.config

    def save_reviews(self, reviews, platform):
        """Save reviews to a JSON file."""

        restaurant_folder_name = self.restaurant_name.replace(" ", "_").lower().replace("'", "")
        
        # create folder for each restaurant
        os.makedirs(f"{self.output_path}/{restaurant_folder_name}", exist_ok=True)

        # Save reviews to JSON
        file_path = f"{self.output_path}/{restaurant_folder_name}/{platform}_reviews.json"
        with open(file_path, "w") as f:
            json.dump(reviews, f, indent=2)

    def crawl(self):
        """To be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement this method")
