"""A complete end-to-end test for an e-commerce website."""
from seleniumbase import BaseCase, SB
BaseCase.main(__name__, __file__)
import random
import json


class MyTestClass(BaseCase):

    def test_swag_labs(self):
        self.maximize_window()
        name = "Thai Basil"
        location = "Tempe"
        name = name.replace(" ", "+").lower().strip()
        location = location.replace(" ", "+").lower().strip()
        name = name + "+" + location
        self.open(f"https://www.google.com/maps/search/{name}")

        self.wait(random.randint(1, 2))

        # click on first restaurant
        if self.is_element_visible("//h1[contains(text(),'Results')]/../../../../div[3]/div/a"):
            self.click("//h1[contains(text(),'Results')]/../../../../div[3]/div/a")
        
        self.wait(random.randint(1, 2))

        # click on reviews
        self.click("//button/div/div[contains(text(),'Reviews')]")


        self.wait(random.randint(1, 2))

        self.scroll_into_view("//*[contains(@aria-label, 'Refine reviews')]/../div[8]")

        self.wait(random.randint(1, 2))
        self.scroll_into_view("//*[contains(@aria-label, 'Refine reviews')]/../div[9]")

        # get the class name of one review block
        review_block_class = str(self.get_attribute("//*[contains(@aria-label, 'Refine reviews')]/../div[9]/div[1]/div/div", 'class'))

        reviews = []
        count = 1
        while count < 3:
            # get name of the reviewer
            self.scroll_into_view(f"(//*[contains(@class, '{review_block_class}')])[{count}]/div[2]/div[2]/div[1]/button/div[1]")
            
            self.wait(random.randint(1, 2))
            name = self.get_text(f"(//*[contains(@class, '{review_block_class}')])[{count}]/div[2]/div[2]/div[1]/button/div[1]")
            print(name)

            # get star
            self.scroll_into_view(f"(//*[contains(@class, '{review_block_class}')])[{count}]/div[4]/div/span[1]")
            star = self.get_attribute(f"(//*[contains(@class, '{review_block_class}')])[{count}]/div[4]/div/span[1]", 'aria-label') 
            print(star)
            # get date
            date = self.get_text(f"(//*[contains(@class, '{review_block_class}')])[{count}]/div[4]/div/span[2]")
            print(date)

            # check if more button present
            # if self.is_element_present(f"((//*[contains(@class, '{review_block_class}')])[{count}]/div[4]/div[2]/div/span[2]/button"):
            self.click(f"(//*[contains(@class, '{review_block_class}')])[{count}]/div[4]/div[2]/div/span[2]/button")
            

            self.wait(random.randint(1, 2))
            # get review
            review = self.get_text(f"(//*[contains(@class, '{review_block_class}')])[{count}]/div[4]/div[2]/div[1]/span")
            print(review)

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