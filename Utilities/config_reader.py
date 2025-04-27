import configparser
import os

class ConfigReader:

    def __init__(self, filepath=None):
        if filepath is None:
            filepath = os.path.join(os.path.dirname(__file__), '..', 'Config', 'config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(filepath)

    def get(self, key):
        return self.config['DEFAULT'][key]