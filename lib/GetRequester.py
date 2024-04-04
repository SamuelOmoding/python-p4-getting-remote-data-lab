import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        # Return the content of the response as bytes
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        # Decode bytes to string
        response_body_str = response_body.decode('utf-8')
        # Parse the string as JSON and return
        return eval(response_body_str)
