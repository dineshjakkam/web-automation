from models import Browser
from models import GoogleSearch

browser = Browser()
tab = browser.open_new_tab(incognito=True)
GoogleSearch(tab).search("amazon.com")