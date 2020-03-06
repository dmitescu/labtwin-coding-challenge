import requests

# Could as well be a REST call
class BERTRequest():
    def __init__(self, proc_req):
        self.body = proc_req.body
        self.ratio = proc_req.ratio
        self.min_length = proc_req.min_length
        self.max_length = proc_req.max_length

    def request(self):
        return "processed"
        
