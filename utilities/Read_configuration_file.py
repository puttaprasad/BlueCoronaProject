import configparser

import configurations


def read_configuration_file(category, key):
    config = configparser.ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category,key)