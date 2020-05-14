import os
import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from common.utils import get_pwd, is_balena
from common import WALogger

logger = WALogger.get_logger()


class Browser:
    """Selenium web driver class"""

    _tabs = []

    @classmethod
    def get_tab(cls):
        return cls._tabs[0]

    @property
    def any_tab_available(self):
        return not len(self.__class__._tabs) == 0

    @classmethod
    def open_new_tab(cls, incognito=False, headless=False):
        """
        Open and return new tab
        :param incognito: opens incognito window
        :param headless:  opens headless browser
        :return:
        """
        chrome_options = Options()
        if incognito:
            chrome_options.add_argument("--incognito")
        if headless:
            chrome_options.add_argument("--headless")

        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')

        if not is_balena():
            driver_path = get_pwd() + "/chromedriver"
            tab = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
        else:
            try:
                tab = webdriver.Chrome(options=chrome_options)
            except:
                logger.error("Chrome driver not found")

        cls._tabs.append(tab)

        return tab

    @classmethod
    def close_tab(cls, tab=None):
        """
        Close all the
        :param tab:
        :return:
        """
        if tab is not None:
            tab.close()
            if tab in cls._tabs:
                cls._tabs.remove(tab)

        elif len(cls._tabs):
            tab = cls._tabs.pop(0)
            tab.close()

    @classmethod
    def close_all_tabs(cls):
        while len(cls._tabs):
            tab = cls._tabs.pop(0)
            tab.close()







