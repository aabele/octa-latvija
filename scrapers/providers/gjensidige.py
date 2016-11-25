# -*- coding: utf8 -*-
""" sasfsd"""

from __future__ import unicode_literals



from scrapers.base import OCTAScraper
from selenium.webdriver.common.keys import Keys


class GjensidigeOCTAScraper(OCTAScraper):
    """ IF does not allow to query more than 30 days before the expiration date of the current insurance policy """


    base_url = 'https://www.gjensidige.lv/pirkt-octa/online-service'

    def parse(self, car_number, tech_passport_id):
        """   """

        car_id_input = self.driver.find_element_by_xpath('//input[@id="VehicleRegistrationNumber"]')
        car_id_input.send_keys(car_number)

        tech_passport_id_input = self.driver.find_element_by_xpath('//input[@id="VehicleRegCertificateNumber"]')
        tech_passport_id_input.send_keys(tech_passport_id)

        submit_button = self.driver.find_element_by_xpath('//button[@class="btn next"]')
        submit_button.click()

        self.wait_for_ajax()

        response = []
        return response

