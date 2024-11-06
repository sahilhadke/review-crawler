from .review_crawler import ReviewCrawler
class GoogleCrawler(ReviewCrawler):

    def test_boilerplate(self):
        self.open(self.url)
        self.type('textarea[title="Search"]', "SeleniumBase\n")