import pytest
from lib.GetRequester import GetRequester

class TestGetRequester:
    URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
    JSON_STRING = b"[\n  {\n    \"name\": \"Daniel\",\n    \"occupation\": \"LG Fridge Salesman\"\n  },\n  {\n    \"name\": \"Joe\",\n    \"occupation\": \"WiFi Fixer\"\n  },\n  {\n    \"name\": \"Avi\",\n    \"occupation\": \"DJ\"\n  },\n  {\n    \"name\": \"Howard\",\n    \"occupation\": \"Mountain Legend\"\n  }\n]\n"
    CONVERTED_DATA = [{'name': 'Daniel', 'occupation': 'LG Fridge Salesman'}, 
                      {'name': 'Joe', 'occupation': 'WiFi Fixer'}, 
                      {'name': 'Avi', 'occupation': 'DJ'}, 
                      {'name': 'Howard', 'occupation': 'Mountain Legend'}]

    def test_get_response(self):
        '''get_response_body function returns response.'''
        requester = GetRequester(self.URL)
        assert requester.get_response_body() == self.JSON_STRING

    def test_load_json(self):
        '''load_json function returns response.'''
        requester = GetRequester(self.URL)
        assert requester.load_json() == self.CONVERTED_DATA
