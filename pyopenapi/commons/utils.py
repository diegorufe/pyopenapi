def get_value_dict(key, dic):
    value = None

    if key is not None and dic is not None and key in dic:
        value = dic[key]

    return value
