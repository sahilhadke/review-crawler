# reviewcrawler.py
import json
import time
import random
from seleniumbase import SB


class ReviewCrawler:
    def __init__(self, sleep_time_range=(1, 2)):
        self.sleep_time_range = sleep_time_range

    def save_reviews_to_json(self, reviews, filename):
        """Save reviews to a JSON file."""
        with open(filename, 'w') as file:
            json.dump(reviews, file, indent=4)
        print(f"Saved {len(reviews)} reviews to {filename}")

class GoogleCrawler(ReviewCrawler):
    def __init__(self, max_reviews, restaurant_name, location, sleep_time_range=(1, 2)):
        super().__init__(sleep_time_range)
        self.max_reviews = max_reviews
        self.restaurant_name = restaurant_name
        self.location = location

    def crawl(self):
        reviews = []
        with SB() as sb:  # Opens and closes the Selenium session
            sb.maximize_window()
            name = self.restaurant_name.replace(" ", "+").lower().strip()
            location = self.location.replace(" ", "+").lower().strip()
            sb.open(f"https://www.google.com/maps/search/{name}+{location}")
            sb.wait(2) # mandatory wait
            time.sleep(random.randint(self.sleep_time_range[0], self.sleep_time_range[1]))

            # click on first restaurant
            restaurant_xpath = "//h1[contains(text(),'Results')]/../../../../div[3]/div/a"
            if sb.is_element_visible(restaurant_xpath):
                sb.click(restaurant_xpath)
                sb.wait(2) # mandatory wait
            time.sleep(random.randint(self.sleep_time_range[0], self.sleep_time_range[1]))

            # click on reviews
            review_button_xpath = "//button/div/div[contains(text(),'Reviews')]"
            if sb.is_element_visible(review_button_xpath):
                sb.click(review_button_xpath)
                sb.wait(2) # mandatory wait
                time.sleep(random.randint(self.sleep_time_range[0], self.sleep_time_range[1]))

            else:
                print('No reviews found')
                return
            
            # scroll to reviews
            review_block_xpath = "//*[contains(@aria-label, 'Refine reviews')]/../div[8]"
            sb.scroll_into_view(review_block_xpath)
            sb.wait(1) # mandatory wait
            time.sleep(random.randint(self.sleep_time_range[0], self.sleep_time_range[1]))

            # scroll to revies again
            review_block_xpath = "//*[contains(@aria-label, 'Refine reviews')]/../div[9]"
            sb.scroll_into_view(review_block_xpath)
            sb.wait(1) # mandatory wait
            time.sleep(random.randint(self.sleep_time_range[0], self.sleep_time_range[1]))

            # get review block class name
            review_block_class = "jftiEf"
            
            count = 1
            while count <= self.max_reviews:
                time.sleep(random.randint(self.sleep_time_range[0], self.sleep_time_range[1]))
                name = ""
                review = ""
                star = ""
                date = ""

                # get name of the reviewer
                name_xpath = f"((//*[contains(@class, '{review_block_class}')])[{count}]//button[1])[2]/div[1]"
                if sb.is_element_visible(name_xpath):
                    # srcoll
                    sb.scroll_into_view(name_xpath)
                    name = sb.get_text(name_xpath)
                else:
                    print('Could not retrieve name: ', count)
                    break

                # get star rating
                star_xpath = f"(//*[contains(@class, '{review_block_class}')])[{count}]//span[@role='img']"
                if sb.is_element_visible(star_xpath):
                    # srcoll
                    sb.scroll_into_view(star_xpath)
                    star = sb.get_attribute(star_xpath, 'aria-label')
                else:
                    print('Could not retrieve star rating: ', count)
                    break

                # get date
                date_xpath = f"(//*[contains(@class, '{review_block_class}')])[{count}]//span[@role='img']/../span[2]"
                if sb.is_element_visible(date_xpath):
                    # srcoll
                    sb.scroll_into_view(date_xpath)
                    date = sb.get_text(date_xpath)
                else:
                    print('Could not retrieve date: ', count)
                    break

                # get review
                review_xpath = f"((//*[contains(@class, '{review_block_class}')])[{count}]//div[@class='MyEned']/span)[1]"
                if sb.is_element_visible(review_xpath):
                    # srcoll
                    sb.scroll_into_view(review_xpath)

                    # more button
                    more_button_xpath = f"((//*[contains(@class, '{review_block_class}')])[{count}]//div[@class='MyEned']/span)[2]"
                    if sb.is_element_visible(more_button_xpath):
                        sb.click(more_button_xpath)
                    review = sb.get_text(review_xpath)
                else:
                    print('Could not retrieve review: ', count)
                    break

                # add review to list
                reviews.append({"name": name, "review": review, "star": star, "date": date})
                count += 1

            sb.tearDown()
            self.save_reviews_to_json(reviews, "google_reviews.json")

class YelpCrawler(ReviewCrawler):
    def __init__(self, max_reviews, restaurant_name, location, sleep_time_range=(1, 2)):
        super().__init__(sleep_time_range)
        self.max_reviews = max_reviews
        self.restaurant_name = restaurant_name
        self.location = location

    def crawl(self):
        reviews = []
        with SB() as sb:  # Opens and closes the Selenium session
            
            sb.maximize_window()
            name = self.restaurant_name.replace(" ", "+").lower().strip()
            location = self.location.replace(" ", "+").lower().strip()
            
            sb.open(f"https://www.google.com/search?q={name}+{location}+yelp+reviews")
            sb.wait(2) # mandatory wait

            # click on first google link
            first_link_xpath = "(//*[contains(@class, 'LC20lb')])[1]"
            if sb.is_element_visible(first_link_xpath):
                sb.click(first_link_xpath)
                sb.wait(2) # mandatory wait
            else:
                print('Wrong google search, try different name')
                return
            
            time.sleep(random.randint(self.sleep_time_range[0], self.sleep_time_range[1]))

            # get current url
            url = sb.get_current_url()
            url = url + '#reviews'
            sb.open(url)

            time.sleep(random.randint(self.sleep_time_range[0], self.sleep_time_range[1]))

            count = 1
            current_page = 1
            while count <= self.max_reviews:
                name = ""
                star = ""
                date = ""
                review = ""
                time.sleep(random.randint(self.sleep_time_range[0], self.sleep_time_range[1]))

                if current_page >= 11:
                    # click on next page
                    next_button_xpath = f"//div[@id='reviews']//ul[starts-with(@class, ' list__')]/../div[starts-with(@class, 'pagination__')]//a[starts-with(@class, 'next-link')]"
                    if sb.is_element_visible(next_button_xpath):
                        sb.click(next_button_xpath)
                        time.sleep(random.randint(self.sleep_time_range[0], self.sleep_time_range[1]))
                        current_page = 1
                    else:
                        print('No more pages')
                        break

                # scroll to review block 
                review_count_xpath = f"//div[@id='reviews']//ul[starts-with(@class, ' list__')]/li[{current_page}]"
                if sb.is_element_visible(review_count_xpath):
                    sb.scroll_into_view(review_count_xpath)
                else:
                    print('Could not find review block: ', count)
                    break

                # get name
                name_xpath = f"(//div[@id='reviews']//ul[starts-with(@class, ' list__')]/li[{current_page}]//a[starts-with(@href, '/user_details')])[2]"
                if sb.is_element_visible(name_xpath):
                    name = sb.get_text(name_xpath)
                else:
                    print('Could not retrieve name: ', count)
                    break

                # get star
                star_xpath = f"//div[@id='reviews']//ul[starts-with(@class, ' list__')]/li[{current_page}]//div[starts-with(@role, 'img')]"
                if sb.is_element_visible(star_xpath):
                    star = sb.get_attribute(star_xpath, "aria-label")
                else:
                    print('Could not retrieve star rating: ', count)
                    break

                # get date
                date_xpath = f"//div[@id='reviews']//ul[starts-with(@class, ' list__')]/li[{current_page}]//div[starts-with(@role, 'img')]/../../../../div[2]/span"
                if sb.is_element_visible(date_xpath):
                    date = sb.get_text(date_xpath)
                else:
                    print('Could not retrieve date: ', count)
                    break
            
                # get review
                review_xpath = f"//div[@id='reviews']//ul[starts-with(@class, ' list__')]/li[{current_page}]//p[starts-with(@class, 'comment_')]/span"
                if sb.is_element_visible(review_xpath):
                    review = sb.get_text(review_xpath)
                else:
                    print('Could not retrieve review: ', count)
                    break

                reviews.append({
                    "name": name,
                    "star": star,
                    "date": date,
                    "review": review
                })

                count += 1
                current_page += 1
            
            # tear down
            sb.tearDown()
            self.save_reviews_to_json(reviews, "yelp_reviews.json")