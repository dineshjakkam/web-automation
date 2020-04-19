import os
from instabot import Bot


class InstaBot:
    """
    Instagram bot to post pictures
    """

    def __init__(self):
        """
        Initialize and login to instagram
        """
        self.username = os.environ['INSTA_BOT_ID']
        self.password = os.environ['INSTA_BOT_PSWD']

    def post_picture(self):
        """
        Post picture to instagram using credentials
        :return:
        """
        bot = Bot()
        bot.login(username=self.username,
                  password=self.password)
        text = 'Here you can put your caption for the post'
        bot.upload_photo("final_image.jpg",
                         caption=text)
