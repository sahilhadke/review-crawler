"""A complete end-to-end test for an e-commerce website with UC mode enabled."""
from seleniumbase import BaseCase, SB
import random
import json

class MyTestClass(BaseCase):
    def test_swag_labs(self):
        # Enable UC mode by setting `uc=True`
        with SB(browser="firefox", uc=True) as sb:
            sb.maximize_window()
            name = "Thai Basil"
            location = "Tempe"
            name = name.replace(" ", "+").lower().strip()
            location = location.replace(" ", "+").lower().strip()

            sb.open(f"https://www.google.com/search?q={name}+{location}+yelp+reviews")
            sb.wait(random.randint(2, 5))

            # Click on the first link
            sb.click("(//*[contains(@class, 'LC20lb')])[1]")

            sb.wait(10)
            sb.scroll_into_view("#reviews")

            reviews = []

            count = 1
            while count < 5:
                # Scroll to review count
                if sb.is_element_visible(f"//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[{count}]/div/div/div/div/div/div/div[2]/div/span"):
                    sb.scroll_into_view(f"//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[{count}]/div/div/div/div/div/div/div[2]/div/span")
                    sb.wait(random.randint(2, 5))

                    # Get name of the reviewer
                    reviewer_name = sb.get_text(f"//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[{count}]/div/div/div/div/div/div/div[2]/div/span")
                    sb.wait(random.randint(2, 5))

                    # Get star rating
                    star = sb.get_attribute(f"//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[{count}]/div/div[2]/div/div/div/div/div", 'aria-label')
                    sb.wait(random.randint(2, 5))

                    # Get date
                    date = sb.get_text(f"//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[{count}]/div/div[2]/div/div[2]/span")
                    sb.wait(random.randint(2, 5))

                    # Get review text
                    review = sb.get_text(f"//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[{count}]/div/div[4]/p")
                    sb.wait(random.randint(2, 5))
                    count += 1

                    temp_dict = {
                        "name": reviewer_name,
                        "star": star,
                        "date": date,
                        "review": review
                    }

                    reviews.append(temp_dict)
                else:
                    # Click on next
                    sb.click("//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../div[5]/div/div/*/*/*/*[contains(@class, 'icon--24-chevron-right-v2')]")

            with open("reviews_yelp.json", "w", encoding="utf-8") as file:
                json.dump(reviews, file, ensure_ascii=False, indent=4)

# Run the test case
BaseCase.main(__name__, __file__)