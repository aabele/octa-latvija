# -*- coding: utf8 -*-
""" sasfsd"""

from __future__ import unicode_literals



from scrapers.base import OCTAScraper
from selenium.webdriver.common.keys import Keys


class IfOCTAScraper(OCTAScraper):
    """ IF does not allow to query more than 30 days before the expiration date of the current insurance policy """


    base_url = 'https://web.if.lv/mansif/if/policies/Mtpl/entry.aspx?utm_source=if.lv&utm_medium=octa&utm_content=top&utm_campaign=web_sale'

    def parse(self, car_number, tech_passport_id):
        """   """

        car_id_input = self.driver.find_element_by_xpath('//input[@name="ctl00$ctl00$masterPlhContent$ContentPlaceHolder2$txtRegNr"]')
        car_id_input.send_keys(car_number)

        tech_passport_id_input = self.driver.find_element_by_xpath('//input[@id="ctl00_ctl00_masterPlhContent_ContentPlaceHolder2_txtCertNr"]')
        tech_passport_id_input.send_keys(tech_passport_id)

        terms = self.driver.find_element_by_xpath('//label[@for="ctl00_ctl00_masterPlhContent_ContentPlaceHolder2_chbReadTerms"]')
        terms.click()

        submit_button = self.driver.find_element_by_xpath('//input[@id="ctl00_ctl00_masterPlhContent_ContentPlaceHolder2_btnSearchNew"]')
        submit_button.click()

        self.wait_for_ajax()

        response = []
        return response

