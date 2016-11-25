# -*- coding: utf8 -*-
"""
Gjensidige website scraper
"""

from __future__ import unicode_literals

from scrapers.base import OCTAScraper


class GjensidigeOCTAScraper(OCTAScraper):
    """
    Gjensidige scraper class
    """

    base_url = 'https://www.gjensidige.lv/pirkt-octa/online-service'
    car_id_xpath = '//input[@id="VehicleRegistrationNumber"]'
    passport_id_xpath = '//input[@id="VehicleRegCertificateNumber"]'
    submit_button_xpath = '//button[@class="btn next"]'

    def parse_results(self):
        """
        Parse website insurance offer details

        :return: list of containing prices [3months, 6months, 9months, 12months]
        """
        response = []
        items = self.driver.find_elements_by_xpath('//div[@id="packages"]//span[@style="font-size:18px;"]')
        for item in items:
            response.append(item.text.split(' ')[0])
        return response