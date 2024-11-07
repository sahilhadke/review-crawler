"""A complete end-to-end test for an e-commerce website."""
from seleniumbase import BaseCase, SB
BaseCase.main(__name__, __file__)
import random
import json


class MyTestClass(BaseCase):

    def test_swag_labs(self):
        
        self.maximize_window()
        
        name = "Tha Dhaba"
        location = "tempe"
        name = name.replace(" ", "+").lower().strip()
        location = location.replace(" ", "+").lower().strip()
       
        self.open(f"https://www.google.com/search?q={name}+{location}+yelp+reviews")

        self.wait(random.randint(3, 6))

        # click on first google link
        if self.is_element_visible("(//*[contains(@class, 'LC20lb')])[1]"):
            self.click("(//*[contains(@class, 'LC20lb')])[1]")
        else:
            print('Wrong google search, try different name')
            return
        
        self.wait(random.randint(3, 6))

        # get current url
        url = self.get_current_url()
        url = url + '#reviews'
        self.open(url)

        self.wait(random.randint(5, 10))
        reviews = []

        count = 1
        current_page = 1
        while count < 15:

            name = ""
            star = ""
            date = ""
            review = ""

            
            if current_page >= 10:
                # press next button
                next_button_xpath = f"//div[@id='reviews']//ul[starts-with(@class, ' list__')]/../div[starts-with(@class, 'pagination__')]//a[starts-with(@class, 'next-link')]"
                if self.is_element_visible(next_button_xpath):
                    self.click(next_button_xpath)
                    self.wait(random.randint(3, 6))
                    current_page = 1
                else:
                    print('No next button found')
                    break


            # scroll to review count
            review_count_xpath = f"//div[@id='reviews']//ul[starts-with(@class, ' list__')]/li[{current_page}]"
            if self.is_element_visible(review_count_xpath):
                self.scroll_into_view(review_count_xpath)
                self.wait(random.randint(3, 6))
            else:
                print('No review count found')
                break

            # get name
            name_xpath = f"(//div[@id='reviews']//ul[starts-with(@class, ' list__')]/li[{current_page}]//a[starts-with(@href, '/user_details')])[2]"
            if self.is_element_visible(name_xpath):
                name = self.get_text(name_xpath)
            else:
                print('No name found')
                break

            # get star
            star_xpath = f"//div[@id='reviews']//ul[starts-with(@class, ' list__')]/li[{current_page}]//div[starts-with(@role, 'img')]"
            if self.is_element_visible(star_xpath):
                star = self.get_attribute(star_xpath, "aria-label")
                
            else:
                print('No star found')
                break

            # get date
            date_xpath = f"//div[@id='reviews']//ul[starts-with(@class, ' list__')]/li[{current_page}]//div[starts-with(@role, 'img')]/../../../../div[2]/span"
            if self.is_element_visible(date_xpath):
                date = self.get_text(date_xpath)
            else:
                print('No date found')
                break

            # get review
            review_xpath = f"//div[@id='reviews']//ul[starts-with(@class, ' list__')]/li[{current_page}]//p[starts-with(@class, 'comment_')]/span"
            if self.is_element_visible(review_xpath):
                review = self.get_text(review_xpath)
            else:
                print('No review found')
                break

            self.wait(random.randint(3, 6))

            reviews.append({
                "name": name,
                "star": star,
                "date": date,
                "review": review
            })

            count += 1
            current_page += 1   

        print(reviews)

        with open("reviews_yelp.json", "w", encoding="utf-8") as file:
            json.dump(reviews, file, ensure_ascii=False, indent=4)
