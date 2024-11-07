"""A complete end-to-end test for an e-commerce website."""
from seleniumbase import BaseCase, SB
BaseCase.main(__name__, __file__)
import random
import json


class MyTestClass(BaseCase):

    def test_swag_labs(self):
        self.maximize_window()
        name = "Advertiser+Advisors+LLC"
        location = "tempe"
        name = name.replace(" ", "+").lower().strip()
        location = location.replace(" ", "+").lower().strip()
        name = name + "+" + location
        self.open(f"https://www.google.com/maps/search/{name}")

        self.wait(random.randint(1, 2))

        # click on first restaurant
        restaurant_xpath = "//h1[contains(text(),'Results')]/../../../../div[3]/div/a"
        if self.is_element_visible(restaurant_xpath):
            self.click(restaurant_xpath)
        
        self.wait(random.randint(1, 2))

        # click on reviews
        review_button_xpath = "//button/div/div[contains(text(),'Reviews')]"
        if self.is_element_visible(review_button_xpath):
            self.click(review_button_xpath)
            self.wait(random.randint(1, 2))
        else:
            print('No reviews found')
            return


        # scroll to reviews
        review_block_xpath = "//*[contains(@aria-label, 'Refine reviews')]/../div[8]"
        if self.is_element_visible(review_block_xpath):
            self.scroll_into_view(review_block_xpath)
            self.wait(random.randint(1, 2))
        else:
            # print('No reviews found')
            # return
            pass
        
        # scroll to reviews
        review_block_xpath = "//*[contains(@aria-label, 'Refine reviews')]/../div[9]"
        if self.is_element_visible(review_block_xpath):
            self.scroll_into_view(review_block_xpath)
            self.wait(random.randint(1, 2))
        else:
            # print('No reviews found')
            # return
            pass
        
        review_block_class = "jftiEf"
        # get the class name of one review block
        review_block_class_xpath = "//*[contains(text(), 'Sort') and contains(@class, 'fontTitleSmall')]/../../../../../../div[3]/div[8]/div[1]"
        if self.is_element_visible(review_block_class_xpath):
            review_block_class = str(self.get_attribute(review_block_class_xpath, 'class'))
        
        reviews = []
        count = 1
        while count < 15+1:
            
            name = ""
            star = ""
            date = ""
            review = ""

            # get name of the reviewer
            name_xpath = f"((//*[contains(@class, '{review_block_class}')])[{count}]//button[1])[2]/div[1]"
            if self.is_element_visible(name_xpath):
                self.scroll_into_view(name_xpath)
                self.wait(random.randint(1, 2))
                name = self.get_text(name_xpath)
                 
            else:
                print('Could not retrieve name: ', count)
                break

            # get star
            star_xpath = f"(//*[contains(@class, '{review_block_class}')])[{count}]//span[@role='img']"
            if self.is_element_visible(star_xpath):
                self.scroll_into_view(star_xpath)
                star = self.get_attribute(star_xpath, 'aria-label')
            else:
                print('Could not retrieve star: ', count)
                break

            # get date
            date_xpath = f"(//*[contains(@class, '{review_block_class}')])[{count}]//span[@role='img']/../span[2]"
            if self.is_element_visible(date_xpath):
                self.scroll_into_view(date_xpath)
                date = self.get_text(date_xpath)
            else:
                print('Could not retrieve date: ', count)
                break

            # get review
            review_xpath = f"((//*[contains(@class, '{review_block_class}')])[{count}]//div[@class='MyEned']/span)[1]"
            if self.is_element_visible(review_xpath):
                self.scroll_into_view(review_xpath)
                
                # click on more button
                more_button_xpath = f"((//*[contains(@class, '{review_block_class}')])[{count}]//div[@class='MyEned']/span)[2]"
                if self.is_element_visible(more_button_xpath):
                    self.click(more_button_xpath)
                review = self.get_text(review_xpath)
            else:
                print('Could not retrieve review: ', count)
                break

            temp = {
                "name": name,
                "star": star,
                "date": date,
                "review": review
            }
            reviews.append(temp)
            count += 1

        print(reviews)

        # next button
        # //*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../div[5]/div/div/*/*/*/*[contains(@class, 'icon--24-chevron-right-v2')]
        # name - //*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[1]/div/div/div/div/div/div/div[2]/div/span
        # star - //*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[1]/div/div[2]/div/div/div/div/div
        # date - //*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[1]/div/div[2]/div/div[2]/span
        # review - //*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[1]/div/div[4]/p
        with open("reviews.json", "w", encoding="utf-8") as file:
            json.dump(reviews, file, ensure_ascii=False, indent=4)
