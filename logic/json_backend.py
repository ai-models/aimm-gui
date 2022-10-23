import json
import os


class JsonHandler:
    @staticmethod
    def get_models():
        parent = os.getcwd()
        models_json = open(f"models.json")
        data = json.load(models_json)
        return data
