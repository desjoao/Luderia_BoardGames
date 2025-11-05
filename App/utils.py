import os
import json
from cryptography.fernet import Fernet

class Utils:
    def __init__(self):
        self.__version__ = "1.0.0.0"
    
    def read_json(self, name: str):
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            file_name = name + '.json'
            path_json = os.path.join(path, file_name)
            with open(path_json, encoding = 'utf-8') as json_file:
                return json.load(json_file)
        
        except FileNotFoundError as e:
            msg = f'Arquivo {name} não encontrado.'
            print(msg)
            return None