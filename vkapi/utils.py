# -*- coding: utf-8 -*-

# from vkapi import const
# from vkapi.exceptions import VKUnknownMethod


def py_name_to_method(name):
    words = name.split('_')
    if len(words) == 1:
        method_name = words[0]
    else:
        method_name = words[0] + '.' + words[1]
        for word in words[2:]:
            method_name += word[0].upper() + word[1:]

    # if method_name not in const.ALL_METHODS:
        # raise VKUnknownMethod(name, method_name)
    return method_name


def normalize_param(param):
    try:
        return ','.join(str(p) for p in param)
    except:
        return str(param)


def prepare_params(params):
    result = {k: normalize_param(v) for k, v in params.items()}
    return result
