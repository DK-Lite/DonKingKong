import json, re
from os import path

class Loader:

    def __init__(self):
        abs_path = path.dirname(path.realpath(__file__))

        with open(path.join(abs_path, "files/configs.json")) as r_file: 
            self.configs = json.load(r_file)

        with open(path.join(abs_path, "files/areacode.txt"), 'r') as r_file: 
            self.codes = r_file.readlines()

    def get_codes(self):
        return [ re.sub(r'[\n]*', '', code) for code in self.codes ]

    def get_configs(self):
        return self.configs
