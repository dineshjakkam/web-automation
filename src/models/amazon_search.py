from selenium.webdriver.common.keys import Keys


class AmazonSearch:

    def __init__(self, tab):
        self.tab = tab
        self.tab.get("https://www.amazon.com")

    def search(self, value):
        search_bar = self.tab.find_element_by_id('twotabsearchtextbox')
        search_bar.send_keys(value)
        search_bar.send_keys(Keys.ENTER)

    def fetch_all_items(self):
        elements = self.tab.find_elements_by_class_name('sg-col-inner')
        for elem in elements:
            try:
                name = elem.find_elements_by_class_name('s-image')[0].get_attribute('alt')
                price_dollars = elem.find_elements_by_class_name('a-price')[0].text[:-3]
                price_cents = elem.find_elements_by_class_name('a-price')[0].text[-2:]
                rating = elem.find_elements_by_class_name('a-row.a-size-small')[0]
                total_price = price_dollars+'.'+price_cents
                print(rating.text)
                #print("{}-{}".format(name, total_price))
            except IndexError:
                pass
