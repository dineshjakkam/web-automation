import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.common.by import By


def name_check(movie_name):
    if re.search("[^a-zA-Z0-9\n\s\.]", movie_name) == None:
        print("Given Movie name is a valid one")
        crt_name = movie_name.lower()
        return crt_name
        
    else:
        print("Given movie name has junk characters, so removing those")
        crt_name = re.sub("[^a-zA-Z0-9\n\s\.]", "", movie_name).lower()
        print(crt_name)
        return crt_name


def len_check(movie_name):
    s = len(movie_name.strip())
    #print(s)
    if s == 0:
        print("No Input Received")
        movie_name = input("Enter a Movie Name: ")
        len_check(movie_name)
    else:
        print("Entered else block")
        #global act_name
        #act_name = name_check(movie_name)
        return name_check(movie_name)
        print(name_check(movie_name))

while True:
    movie_name = input("Enter a Movie Name: ")
    act_name = len_check(movie_name)
    print(act_name)

    print("Do you mean " + act_name)
    user_input = input()
    if user_input.lower() == 'y':
        print("Confirmed the movie name")
        break
#    else:
#       movie_name = input("Re-enter a Movie Name: ")
        #len_check(movie_name)
        #act_name = name_check(movie_name)


chrome_options = Options()
#chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(executable_path="/Users/19713/Documents/chromedriver", options=chrome_options)
browser.get("https://www.google.com")
time.sleep(3)
#search_bar = browser.find_element_by_class_name("yt-simple-endpoint style-scope ytd-button-renderer")
search_bar = browser.find_element("name", "q")
search_bar.send_keys('movierulz')
search_bar.send_keys(Keys.ENTER)


elems = browser.find_elements("xpath", "//*[@href]")
for elem in elems:
    if "movierulz." in elem.get_attribute("href"):
        browser.get(elem.get_attribute("href"))
        break

time.sleep(5)
search_bar = browser.find_element("name", "s")
print("type in search bar")
search_bar.send_keys(act_name)
search_bar.send_keys(Keys.ENTER)

elems = browser.find_elements("xpath", "//*[@href]")
for elem in elems:
    if movie_name in elem.get_attribute("title").lower() and "search" not in elem.get_attribute("href"):
        browser.get(elem.get_attribute("href"))
        break

elems = browser.find_elements(By.TAG_NAME, "p")
for elem in elems:
    #print(elem)
    if "Download" in elem.text:
        e = elem.find_elements(By.TAG_NAME, "a")
        browser.get(e[0].get_attribute("href"))
        break

time.sleep(4)

elem = browser.find_element(By.CLASS_NAME, "download-button")
embed_elem = elem.find_element(By.TAG_NAME, "a")
link = embed_elem.get_attribute("href")
browser.get(link)

#browser.get(browser.find_element(By.CLASS_NAME, "download").find_element(By.TAG_NAME, "a").get_attribute("href"))

#browser.find_element(By.CLASS_NAME, "download").find_element(By.TAG_NAME, "a").click()

time.sleep(6)

browser.find_element("xpath", "//a[@id='downloadvideo']").click()
time.sleep(5)

#elem = browser.find_element(By.CLASS_NAME, "download").find_element(By.TAG_NAME, "a").get_attribute("href")

#print(elem)

#browser.get(elem)

