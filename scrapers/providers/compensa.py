# -*- coding: utf8 -*-
"""
Compensa website scraper
"""

from __future__ import unicode_literals

import random

from scrapers.base import OCTAScraper
from selenium.webdriver.common.keys import Keys


class CompensaOCTAScraper(OCTAScraper):
    """
    Compensa scraper class
    """

    base_url = 'http://online.compensa.lv/lv/Octa'
    car_id_xpath = '//input[@name="PlateNumber"]'
    passport_id_xpath = '//input[@name="CertNumber"]'
    submit_button_xpath = '//input[@type="submit"]'
    extra_field_xpath = '//input[@name="Phone"]'
    extra_field_value = random.randint(10000000, 99999999)
    accept_terms_xpath = '//label[@for="AgreeToUseData"]/span'
    change_trigger_key = Keys.TAB
    results_loaded_text = '9 mēneši'

    def _parse_results(self):
        """
        Parse website insurance offer details

        :return: list of containing prices [3months, 6months, 9months, 12months]
        """
        response = []
        for block in self.driver.find_elements_by_xpath('//div[@class="floatBlock2"]'):
            part1 = block.find_element_by_xpath('.//h1')
            part2 = block.find_element_by_xpath('.//p')
            response.append('%s.%s' % (part1.text.replace(',', ''), part2.text.split(' ')[0]))
        return response
