# -*- coding: utf8 -*-
"""
IF website scraper
"""

from __future__ import unicode_literals

from scrapers.base import OCTAScraper


class IfOCTAScraper(OCTAScraper):
    """
    IF scraper class

    IF does not allow to query more than 30 days before the
    expiration date of the current insurance policy
    """

    base_url = 'https://web.if.lv/mansif/if/policies/Mtpl/entry.aspx'
    car_id_xpath = '//input[@name="ctl00$ctl00$masterPlhContent$ContentPlaceHolder2$txtRegNr"]'
    passport_id_xpath = '//input[@id="ctl00_ctl00_masterPlhContent_ContentPlaceHolder2_txtCertNr"]'
    submit_button_xpath = '//input[@id="ctl00_ctl00_masterPlhContent_ContentPlaceHolder2_btnSearchNew"]'

    def parse(self):
        """   """

        response = []
        return response

