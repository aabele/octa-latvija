# -*- coding: utf8 -*-
"""
Gjensidige website scraper
"""

from __future__ import unicode_literals

from scrapers.base import OCTAScraper


class GjensidigeOCTAScraper(OCTAScraper):
    """
    Gjensidige scraper class

    Gjensidige does not allow to query more than 30 days before the expiration
    date of the current insurance policy
    """

    base_url = 'https://www.gjensidige.lv/pirkt-octa/online-service'
    car_id_xpath = '//input[@id="VehicleRegistrationNumber"]'
    passport_id_xpath = '//input[@id="VehicleRegCertificateNumber"]'
    submit_button_xpath = '//button[@class="btn next"]'
