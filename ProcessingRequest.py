import json

class InvalidData(Exception):
    pass

class ProcessingRequest():
    def __init__(self, body, ratio, min_length, max_length):
        self.body = body
        self.ratio = ratio
        self.min_length = min_length
        self.max_length = max_length

    def from_json(self, json_dict):
        if "body" in json_dict.keys():
            self.body = json_dict["body"]
        if "ratio" in json_dict.keys():
            self.ratio = json_dict["ratio"]
        if "min_length" in json_dict.keys():
            self.min_length = json_dict["min_length"]
        if "max_length" in json_dict.keys():
            self.max_length = json_dict["max_length"]
        if not isinstance(self.body, str):
            raise InvalidData()
        if not isinstance(self.ratio, float):
            raise InvalidData()
        if not isinstance(self.min_length, int):
            raise InvalidData()
        if not isinstance(self.max_length, int):
            raise InvalidData()

