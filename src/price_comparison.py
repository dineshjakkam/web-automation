from models import Browser
from models import AmazonSearch

browser = Browser()
tab = browser.open_new_tab(incognito=True)
amazon = AmazonSearch(tab)
amazon.search("Apple ipad pro 10.2 inch")
amazon.fetch_all_items()
