import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

movie_name = "amrutham"
chrome_options = Options()
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(executable_path="/Users/venkatadineshjakkampudi/Downloads/chromedriver", options=chrome_options)
browser.get("https://www.google.com")
search_bar = browser.find_element_by_name('q')
search_bar.send_keys('movierulz')
search_bar.send_keys(Keys.ENTER)


elems = browser.find_elements_by_xpath("//*[@href]")
for elem in elems:
    if "movierulz." in elem.get_attribute("href"):
        browser.get(elem.get_attribute("href"))
        break

time.sleep(1)
search_bar = browser.find_element_by_name('s')
search_bar.send_keys(movie_name)
search_bar.send_keys(Keys.ENTER)

elems = browser.find_elements_by_xpath("//*[@href]")
for elem in elems:
    if movie_name in elem.get_attribute("href") and "search" not in elem.get_attribute("href"):
        browser.get(elem.get_attribute("href"))
        break

elems = browser.find_elements_by_tag_name('p')
for elem in elems:
    if "Download" in elem.text:
        e = elem.find_elements_by_tag_name('a')
        browser.get(e[0].get_attribute("href"))
        break

elem = browser.find_element_by_class_name("download-button")
embed_elem = elem.find_element_by_tag_name('a')
link = embed_elem.get_attribute("href")
browser.get(link)

browser.get(browser.find_element_by_class_name("download").find_element_by_tag_name('a').get_attribute("href"))

browser.find_element_by_class_name("download").find_element_by_tag_name('a').click()

time.sleep(5)

elem = browser.find_element_by_class_name("download").find_element_by_tag_name('a').get_attribute("href")

print(elem)

#browser.get(elem)

