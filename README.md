# review-crawler
A web scraper for extracting reviews from websites.

## Installation

* Clone the repository
* Install the dependencies with `pip install -r requirements.txt`

## Usage

* Run `python3 main.py` to start the scraper
* The scraper will output the reviews to a JSON file in the `output` directory

## Demo
[Demo Video](https://youtu.be/0Ls05N8h98Y)

## Configuration
* The following variables are configurable in the `main.py` file:
	+ `crawler_type`: specifies which crawler to use, can be "google", "yelp", or "both"
	+ `max_reviews`: specifies the maximum number of reviews to crawl
	+ `restaurant_name`: specifies the name of the restaurant to crawl
	+ `location`: specifies the location of the restaurant
	+ `min_sleep_time` and `max_sleep_time`: specify the minimum and maximum time to sleep between requests in seconds
	+ `max_tries`: specifies the number of times to retry if Yelp blocks the IP

## Notes
* Yelp seems to block bots after a few requests. I have implemented a retry mechanism for this which will try again after a few seconds. This can be configured in the `main.py` file.
* Additionally, I have implemented a random delay for each request to try to avoid being blocked.
* To further avoid being blocked, I am using Google as a proxy to get to Yelp. So instead of going directly to yelp.com, I am going to Google and searching for "<business name> yelp reviews" and then clicking on the first result.