
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class OCTAScraper(object):
    """
    Scraper base class
    """

    def __init__(self):
        """"""
        self.driver = webdriver.Firefox(executable_path='/home/aivis/Projects/octa-latvia/node_modules/geckodriver/bin/geckodriver')
        self.driver.get(self.base_url)

    def wait_for_ajax(self):
        time.sleep(20)

    def __del__(self):
        """
        Garbage collector
        """
        self.driver.quit()
