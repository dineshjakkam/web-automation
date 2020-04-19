"""
https://www.w3schools.com/cssref/css_colors.asp: CSS colors
PYTHONPATH=. ~/.pyenv/versions/3.7.0/envs/myproject/bin/python3.7 remittance/main.py
"""

import os
import time
from PIL import Image, ImageDraw, ImageFilter

from common import Browser, WALogger
from remittance import AllRates, BuildImage
from remittance.modules import InstaBot
from common.utils import get_pwd

logger = WALogger.get_logger()


def build_new_html_page(rates):
    """
    Read the existing html page and edit with the available rates and write back to new file
    :return:
    """
    html_page_path = get_pwd() + "/remittance/html_pages/image.html"
    update_page = get_pwd() + "/remittance/html_pages/new_image.html"
    with open(html_page_path, 'r', encoding='utf-8') as url:
        page = url.read()
    new_page = BuildImage(page, rates).get_image()
    with open(update_page, 'w', encoding='utf-8') as url:
        url.write(new_page)


def build_image(tab):
    """
    Open the html page, take a screen shot and crop the image.
    :return:
    """
    file_path = "file://" + get_pwd() + "/remittance/html_pages/new_image.html"
    tab.get(file_path)
    tab.save_screenshot("screenshot.png")

    im = Image.open(r"screenshot.png")
    width, height = im.size

    top = 0
    bottom = height*0.6
    left = 0
    right = width*0.525

    im = im.crop((left, top, right, bottom))
    rgb_im = im.convert('RGB')
    rgb_im.save("final_image.jpg")


def loop(tab):
    """
    Run this in loop
    :return:
    """
    try:
        logger.debug("Entering next round polling")
        all_rates = AllRates()
        all_rates.fetch_all_rates(tab)
        status = all_rates.check_if_values_changes()
        if status:
            logger.debug("Values changed status: {}".format(status))
            build_new_html_page(all_rates)
            build_image(tab)
            InstaBot().post_picture()
    except Exception as e:
        logger.error("Exception in loop: {}".format(e))


def main():
    """
    TO run this file sourcing root as src
    sudo PYTHONPATH=. ~/.pyenv/versions/3.7.0/envs/myproject/bin/python3.7 remittance/main.py
    :return:
    """
    try:
        logger.error("=== Starting application ===")
        tab = Browser.open_new_tab(incognito=True, headless=True)
        polling_period = os.environ.get('POLLING_PERIOD', 60)
        while True:
            loop(tab)
            time.sleep(60*polling_period)

    except Exception as e:
        print(e)
        logger.error("Main loop crashed: {}".format(e))


if __name__ == '__main__':
    main()
