from selenium.webdriver.common.keys import Keys


class GoogleSearch:

    def __init__(self, tab):
        self.tab = tab
        self.tab.get("https://www.google.com")

    def search(self, value):
        search_bar = self.tab.find_element_by_name('q')
        search_bar.send_keys(value)
        search_bar.send_keys(Keys.ENTER)
