# -*- coding: utf-8 -*-


class VKResponseError(Exception):

    def __init__(self, response):
        self.response = response

    def __str__(self):
        return str(self.response).encode('utf-8')


class VKUnknownMethod(Exception):

    def __init__(self, name, method_name):
        self.name = name
        self.method_name = method_name

    def __str__(self):
        message = '%s translated to "%s"' % (str(self.name), str(self.method_name))
        return message.encode('utf-8')
