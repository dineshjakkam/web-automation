import os
import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from models.utils import get_pwd


class Browser:
    """Returns selenium web driver instance"""

    _tabs = []

    def __init__(self):
        pass

    @classmethod
    def get_tab(cls):
        return cls._tabs[0]

    @property
    def any_tab_available(self):
        return not len(self.__class__._tabs) == 0

    def open_new_tab(self, incognito=False, headless=False):
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

        driver_path = get_pwd() + "/chromedriver"

        if platform.system() == 'Darwin' and os.path.exists(driver_path):
            tab = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
            self.__class__._tabs.append(tab)
            return tab
        elif not platform.system() == 'Darwin':
            tab = webdriver.Chrome(options=chrome_options)
            self.__class__._tabs.append(tab)
            return tab
        else:
            raise ValueError("Web driver not available")

    @classmethod
    def close_tab(cls, tab=None):
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







