from configparser import ConfigParser


def read_configurations(category, key):
    config = ConfigParser()
    config.read("configuration/config.ini")
    return config.get(category, key)



