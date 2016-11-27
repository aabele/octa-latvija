# -*- coding:utf8 -*-
"""
OCTA data scraper scripts collection
"""

from scrapers.providers.baltikums import BaltikumsOCTAScraper
from scrapers.providers.compensa import CompensaOCTAScraper
from scrapers.providers.gjensidige import GjensidigeOCTAScraper
from scrapers.providers.if_company import IfOCTAScraper
from scrapers.providers.seesam import SeesamOCTAScraper

class_map = {
    'baltikums': BaltikumsOCTAScraper,
    'compensa': CompensaOCTAScraper,
    'gjensidige': GjensidigeOCTAScraper,
    'if_company': IfOCTAScraper,
    'seesam': SeesamOCTAScraper
}


def query_octa_providers(provider, car_id, passport_id):
    """

    :param provider:
    :param car_id:
    :param passport_id:
    :return:
    """
    scraper_class = class_map.get(provider)
    if not scraper_class:
        raise Exception("Can't find such provider")

    scraper = scraper_class(car_id, passport_id)
    return scraper.get_data()