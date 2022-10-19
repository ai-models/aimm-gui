class Json_Handler:
    def get_models(self):
        import json
        import os
        parent = os.getcwd()

        models_json = open(f"{parent}/models.json")

        data = json.load(models_json)

        return data
