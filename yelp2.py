from seleniumbase import Driver
import random 
import time

name = "Thai Basil"
location = "Tempe"

name = name.replace(" ", "+").lower().strip()
location = location.replace(" ", "+").lower().strip()

driver = Driver(browser='firefox', uc=True)
driver.get(f"https://www.google.com/search?q={name}+{location}+yelp+reviews")

time.sleep(random.randint(2, 5))

driver.click("(//*[contains(@class, 'LC20lb')])[1]")
time.sleep(random.randint(7,10))


driver.scroll_to("#reviews")

reviews = []

count = 1
while count < 5:

    # scroll to review count
    if driver.is_element_visible(f"//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[{count}]/div/div/div/div/div/div/div[2]/div/span"):
        driver.scroll_to(f"//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[{count}]/div/div/div/div/div/div/div[2]/div/span")
        time.sleep(random.randint(2, 5))

        # get name of the reviewer
        name = driver.get_text(f"//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[{count}]/div/div/div/div/div/div/div[2]/div/span")
        time.sleep(random.randint(2, 5))

        # get review
        review = driver.get_text(f"//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[{count}]/div/div/div/div/div/div/div[2]/div[2]/div[2]/span")
        time.sleep(random.randint(2, 5))

        # get rating    
        rating = driver.get_text(f"//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[{count}]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/span")
        time.sleep(random.randint(2, 5))

        # get date
        date = driver.get_text(f"//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[{count}]/div/div/div/div/div/div/div[2]/div[2]/div[3]/span")
        time.sleep(random.randint(2, 5))

        # get time
        time = driver.get_text(f"//*[contains(@aria-labelledby, 'inline-search-:rs:')]/../../../../../../../../ul/li[{count}]/div/div/div/div/div/div/div[2]/div[2]/div[4]/span")
        time.sleep(random.randint(2, 5))

        reviews.append({
            "name": name,
            "review": review,
            "rating": rating,
            "date": date,
            "time": time
        })
        count += 1
    else:
        break
print(reviews)



