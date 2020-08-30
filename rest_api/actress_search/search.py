import json
import requests
import random
from .dto.actress_dto import Actress
from django.conf import settings


class SearchActress:

    def __init__(self):
        self.dmm_base_url = 'https://api.dmm.com/affiliate/v3/ActressSearch'
        self.api_id = getattr(settings, "DMM_API_ID", None)
        self.affiliate_id = getattr(settings, "DMM_API_AFFILIATE_ID", None)
        self.dmm_api_url = f'{self.dmm_base_url}?api_id={self.api_id}&affiliate_id={self.affiliate_id}'

    def create_api_url(self, search_prm):
        api_url = self.dmm_api_url
        if search_prm:
            for key, value in search_prm.items():
                search_parameter = f'&{key}={value}'
                api_url = f'{api_url}{search_parameter}'

        return api_url

    def search_actress(self):
        search_prm = {'hits': '1', 'offset': str(random.randint(1, 52456))}
        api_url = self.create_api_url(search_prm)

        response = requests.get(api_url)
        response_json = response.json()
        json_result = response_json['result']
        if json_result['status'] == '200':
            actress_json = json_result['actress']
            return actress_json
