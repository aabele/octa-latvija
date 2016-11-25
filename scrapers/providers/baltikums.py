# -*- coding: utf8 -*-
"""
Baltikums website scraper
"""

from __future__ import unicode_literals

from scrapers.base import OCTAScraper


class BaltikumsOCTAScraper(OCTAScraper):
    """
    Baltikums scraper class
    """

    base_url = 'https://www.polise24.lv/lv/octa-online/'
    car_id_xpath = '//input[@name="regNr"]'
    passport_id_xpath = '//input[@name="aplNr"]'

    def parse_results(self):
        """
        Parse website insurance offer details

        :return: list of containing prices [3months, 6months, 9months, 12months]
        """
        response = []
        items = self.driver.find_elements_by_xpath('//*[@class="priceTableCell"]/div')
        for item in items:
            response.append(item.text.split(' ')[0])
        return response[:4]
