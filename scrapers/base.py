# -*- coding: utf8 -*-
"""
OCTA data scraper base class
"""

from __future__ import unicode_literals

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


_FIREFOX_PATH = '/home/aivis/Projects/octa-latvia/node_modules/geckodriver/bin/geckodriver'


def get_firefox_profile():
    """
    Firefox profile tweaks - does not load images and CSS

    :return: profile instance
    """
    profile = webdriver.FirefoxProfile()
    # profile.set_preference('permissions.default.stylesheet', 2)
    # profile.set_preference('permissions.default.image', 2)
    # profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

    return profile


class OCTAScraper(object):
    """
    Scraper base class
    """

    base_url = ''
    wait_time = 10

    car_id_xpath = ''
    passport_id_xpath = ''
    submit_button_xpath = ''
    accept_terms_xpath = ''
    extra_field_xpath = ''

    extra_field_value = ''

    change_trigger_key = Keys.ENTER

    def __init__(self, car_id, passport_id):
        """

        :param car_id:
        :param passport_id:
        """
        self.car_id = car_id
        self.passport_id = passport_id

        self.driver = webdriver.Firefox(
            firefox_profile=get_firefox_profile(),
            executable_path=_FIREFOX_PATH)
        self.driver.get(self.base_url)

    def __del__(self):
        """
        Garbage collector
        """
        self.driver.quit()

    # Selenium methods

    def wait_for_ajax(self):
        """
        Wait until all AJAX requests are done
        """
        time.sleep(self.wait_time)

    def _scroll_to(self, element):
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)

    def _fill(self, field_xpath, value):
        """
        Find the input field and fill it with specific contents

        :param field_xpath: field xpath filter
        :param value: field value
        """
        input_field = self.driver.find_element_by_xpath(field_xpath)
        self._scroll_to(input_field)
        input_field.send_keys(value)
        input_field.send_keys(self.change_trigger_key)

    def fill_car_id(self):
        """
        Find car id input field and fill it
        """
        if self.car_id_xpath:
            self._fill(self.car_id_xpath, self.car_id)

    def fill_passport_id(self):
        """
        Find passport id input field and fill it
        """
        if self.passport_id_xpath:
            self._fill(self.passport_id_xpath, self.passport_id)

    def fill_extra_field(self):
        """

        :return:
        """
        if self.extra_field_xpath:
            self._fill(self.extra_field_xpath, self.extra_field_value)

    def accept_terms(self):
        """
        Find accept terms checkbox and check it
        """
        if self.accept_terms_xpath:
            input_field = self.driver.find_element_by_xpath(self.accept_terms_xpath)
            self._scroll_to(input_field)
            input_field.click()

    def submit_search_form(self):
        """
        Find form submit button and click it
        """
        if self.submit_button_xpath:
            submit_button = self.driver.find_element_by_xpath(self.submit_button_xpath)
            self._scroll_to(submit_button)
            submit_button.click()
            self.wait_for_ajax()

    def parse_results(self):
        raise NotImplementedError

    def get_data(self):
        """
        Run the selenium commands and parse results

        :return:
        """
        self.fill_car_id()
        self.fill_passport_id()
        self.accept_terms()
        self.fill_extra_field()
        self.submit_search_form()
        self.wait_for_ajax()
        return self.parse_results()

