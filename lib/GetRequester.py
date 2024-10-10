import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve data: {response.status_code}")
        return response.content  # Return response as bytes

    def load_json(self):
        response_body = self.get_response_body()
        return response.json()  # Convert response content to JSON

# Example usage (uncomment to test):
# if __name__ == "__main__":
#     get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
#     json_data = get_requester.load_json()
#     print(json_data)
