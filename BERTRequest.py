from summarizer import Summarizer

# In my opinion for this specific task a REST call
# would have worked better, but for the imaginary scenario
# of this task, where I process text in the api itself,
# this is the way to go
class BERTRequest():
    def __init__(self, proc_req):
        self.body = proc_req.body
        self.ratio = proc_req.ratio
        self.min_length = proc_req.min_length
        self.max_length = proc_req.max_length

    def request(self):
        model = Summarizer()
        result = model(
            self.body,
            ratio=self.ratio,
            min_length=self.min_length,
            max_length=self.max_length)
        text = ''.join(result)
        return text
        
