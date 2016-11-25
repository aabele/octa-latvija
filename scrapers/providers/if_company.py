# -*- coding: utf8 -*-
"""
IF website scraper
"""

from __future__ import unicode_literals

from scrapers.base import OCTAScraper


class IfOCTAScraper(OCTAScraper):
    """
    IF scraper class
    """

    base_url = 'https://web.if.lv/mansif/if/policies/Mtpl/entry.aspx'
    car_id_xpath = '//input[@name="ctl00$ctl00$masterPlhContent$ContentPlaceHolder2$txtRegNr"]'
    passport_id_xpath = '//input[@id="ctl00_ctl00_masterPlhContent_ContentPlaceHolder2_txtCertNr"]'
    submit_button_xpath = '//input[@id="ctl00_ctl00_masterPlhContent_ContentPlaceHolder2_btnSearchNew"]'
    accept_terms_xpath = '//label[@for="ctl00_ctl00_masterPlhContent_ContentPlaceHolder2_chbReadTerms"]'
    results_loaded_text = '9 mēneši'

    def _parse_results(self):
        """
        Parse website insurance offer details

        :return: list of containing prices [3months, 6months, 9months, 12months]
        """
        response = []
        items = self.driver.find_elements_by_xpath('//*[@class="ecmt-text-fat ecmt-text-bold ecmt-text-centered"]/span')
        for item in items:
            response.append(item.text.split(' ')[1])
        return list(reversed(response))
