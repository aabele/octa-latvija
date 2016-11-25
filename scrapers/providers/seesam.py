# -*- coding: utf8 -*-
"""
Seesam website scraper
"""

from __future__ import unicode_literals

from scrapers.base import OCTAScraper


class SeesamOCTAScraper(OCTAScraper):
    """
    Seesam scraper class
    """

    base_url = 'https://www.seesam.lv/polise/#/octa'
    car_id_xpath = '//input[@class="JM"]'
    submit_button_xpath = '//div[@class="DP"]'

    def parse_results(self):
        """
        Parse website insurance offer details
        """
        response = []
        items = self.driver.find_elements_by_xpath('//div[@class="DV CN"]')
        for item in items:
            response.append(item.text.split(' ')[0])
        return response[:4]

