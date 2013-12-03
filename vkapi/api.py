# -*- coding: utf-8 -*-

import time

import requests

from vkapi import const
from vkapi import utils
from vkapi.exceptions import VKResponseError

session = requests.session()


class API(object):
    def __init__(self, access_token=None, lang='ru', v='5.5', https=1):
        self.default_params = {'lang': lang, 'v': v, 'https': https}
        if access_token:
            self.default_params.update({'access_token': access_token})
        t = time.time()
        self._call_time = [t] * 3
        self._public_call_time = [t] * 10

    def __call__(self, method_name, params=None):
        post_data = self.default_params
        if params is not None:
            post_data.update(utils.prepare_params(params))
        url = const.API_URL + method_name
        self._wait_loop(method_name)   # ожидание
        response = session.post(url=url, data=post_data).json()
        # TODO дописать обработку допустимых ошибок
        try:
            return response['response']
        except:
            raise VKResponseError(response)

    def __getattr__(self, name):
        method_name = utils.py_name_to_method(name)

        def method(**params):
            return self(method_name, params)

        self.__dict__.update({name: method})
        return method

    def _wait_loop(self, method_name):
        # ожидание (ограничение на количество запросов в секунду)
        if method_name not in const.PUBLIC_METHODS:
            time.sleep(max(0, self._call_time[0] + 1 - time.time()))
            self._call_time = self._call_time[1:] + [time.time()]
        else:
            time.sleep(max(0, self._public_call_time[0] + 1 - time.time()))
            self._public_call_time = self._public_call_time[1:] + [time.time()]
