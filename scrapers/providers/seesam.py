# -*- coding: utf8 -*-
""" sasfsd"""







from __future__ import unicode_literals



from scrapers.base import OCTAScraper
from selenium.webdriver.common.keys import Keys


class SeesamOCTAScraper(OCTAScraper):
    """ vvveferfferrferr """

    base_url = 'https://www.seesam.lv/polise/'

    def parse(self, car_number):
        """   """
        link_to_octa_page = self.driver.find_element_by_xpath('//div[@class="AK EK"]')
        link_to_octa_page.click()

        car_id_field = self.driver.find_element_by_xpath('//input[@class="JM"]')
        car_id_field.send_keys(car_number)
        car_id_field.send_keys(Keys.ENTER)

        submit_button = self.driver.find_element_by_xpath('//div[@class="DP"]')
        submit_button.click()
        submit_button.send_keys(Keys.ENTER)

        self.wait_for_ajax()

        response = []
        items = self.driver.find_elements_by_xpath('//div[@class="DV CN"]')
        for item in items:
            response.append(item.text.split(' ')[0])

        return response[:4]

