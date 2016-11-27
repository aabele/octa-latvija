# -*- coding:utf8 -*-
"""
Project views
"""

from __future__ import unicode_literals

import random

from django.conf import settings
from django.http.response import JsonResponse
from django.views import View
from django.views.generic.base import TemplateView

from scrapers import query_octa_providers


class ProviderCheck(View):
    """
    OCTA data search backend
    """

    @staticmethod
    def random():
        return random.randint(00, 99)

    def get_random_prices(self):
        return ['%s.%s' % (self.random(), self.random()) for i in range(4)]

    def get(self, request, provider, car_id, certificate_id):
        """

        :param request:
        :param provider:
        :param car_id:
        :param certificate_id:
        :return:
        """

        if settings.DEBUG:
            data = self.get_random_prices()
        else:
            try:
                data = query_octa_providers(provider, car_id, certificate_id)
            except:
                data = []

        return JsonResponse(data, safe=False)


class FrontPage(TemplateView):

    template_name = 'base.html'