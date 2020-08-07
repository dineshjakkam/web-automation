from common.browser import Browser
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
from copy import deepcopy
import pandas as pd

tab = Browser.open_new_tab(incognito=True)
sleep(2)
tab.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = tab.find_element_by_name('username')
username.send_keys('paisatamasha')
password = tab.find_element_by_name('password')
password.send_keys('DINdiv@1')

button_login = tab.find_element_by_xpath('//button[normalize-space()="Log In"]')
button_login.click()
sleep(3)

notnow = tab.find_element_by_xpath('//button[normalize-space()="Not Now"]')
notnow.click()  # comment these last 2 lines out, if you don't get a pop up asking about notifications

sleep(2)
notnow = tab.find_element_by_xpath('//button[normalize-space()="Not Now"]')
notnow.click()  # comment these last 2 lines out, if you don't get a pop up asking about notifications

post_site = "https://www.instagram.com/america_nri_la_frustration/"

prev_user_list = []  # if it's the first time you run it, use this line and comment the two below
# prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,
#                1:2]  # useful to build a user log
# prev_user_list = list(prev_user_list['0'])

new_followed = []
followed = 0
likes = 0
comments = 0
tab.get(post_site)
sleep(5)
try:
    first_thumbnail = tab.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div/div/a/div')
    first_thumbnail.click()
    sleep(randint(2, 4))

    commented_users = tab.find_element_by_class_name("Nm9Fw").find_element_by_tag_name('button').click()
    sleep(randint(1, 5))
    commented_users = tab.find_elements_by_class_name("Jv7Aj.MqpiF  ")
    users = []
    for user in commented_users:
        users.append(deepcopy(user.text))
    print(users)
    for user in users:
        sleep(randint(1, 10))
        link = "https://www.instagram.com/"+user+'/'
        tab.get(link)

    if user not in prev_user_list:
        # If we already follow, do not unfollow
        if tab.find_element_by_class_name("bY2yH").find_element_by_tag_name('button').text == 'Follow':

            tab.find_element_by_class_name("bY2yH").find_element_by_tag_name('button').click()

            new_followed.append(username)
            followed += 1

            # Liking the picture
            button_like = tab.find_element_by_xpath("//*[name()='svg'][@aria-label='Like']")

            button_like.click()
            likes += 1
            sleep(randint(5, 10))

            # Comments and tracker
            comm_prob = randint(1, 10)
            print('{}_{}: {}'.format(hashtag, x, comm_prob))
            comments += 1
            tab.find_element_by_xpath("//*[name()='svg'][@aria-label='Comment']").click()
            comment_box = tab.find_element_by_xpath("//*[name()='textarea'][@aria-label='Add a comment…']")

            if comm_prob < 7:
                comment_box.send_keys('Really cool!')
                sleep(1)
            elif (comm_prob > 6) and (comm_prob < 9):
                comment_box.send_keys('Nice work :)')
                sleep(1)
            elif comm_prob == 9:
                comment_box.send_keys('Nice gallery!!')
                sleep(1)
            elif comm_prob == 10:
                comment_box.send_keys('So cool! :)')
                sleep(1)
            # Enter to post comment
            comment_box.send_keys(Keys.ENTER)
            sleep(randint(22, 28))

        # Next picture
        tab.find_element_by_link_text('Next').click()
        sleep(randint(25, 29))
    else:
        tab.find_element_by_link_text('Next').click()
        sleep(randint(20, 26))
# some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
except Exception as e:
    print(e)

for n in range(0, len(new_followed)):
    prev_user_list.append(new_followed[n])

updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_followed_list_likes.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))