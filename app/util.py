import requests
import openbrewerydb
import json
from itertools import count

BASE_URL = 'https://api.openbrewerydb.org/breweries'



# def _format_request_params(state=None, city=None, brewery_type=None, page=None, per_page=50):
#     params = {
#         'by_state': state,
#         'by_city': city,
#         'by_type': brewery_type
#     }

#     if page is not None:
#         params['page'] = str(page)
#         params['per_page'] = str(per_page)

#     return params

# def _get_request(params=None):
#     response = requests.get(BASE_URL, params=params)
#     return response

# def _get_data(params=None):
#     r = _get_request(params=params)
#     json = r.json()
#     return json

# def load(state=None, city=None, brewery_type=None):
#     data = []
#     num_breweries = 0
#     for page in count(start=1):
#         params = _format_request_params(state=state, city=city, brewery_type=brewery_type, page=page, per_page=50)

#         loaded_data=_get_request(params=params)
#         data.append(loaded_data)
    
#     if not data:
#         raise ValueError('No Data Found in query')
    

#     return data





def get_brew(state):
    res = requests.get(f'{BASE_URL}', params={'by_state':state, 'page':100})
    data = res.json()
    return (data)


def get_state_info(state):
    data = openbrewerydb.load(state=state)
    brewery_types = data['brewery_type'].value_counts()
    # breweryObj = {
    #     'totalBreweries': data.shape[0],
    #     'breweryByType': {
    #         'totalMicro': brewery_types['micro'],
    #         'totalBrewpub': brewery_types['brewpub'],
    #         'totalPlanning': brewery_types['planning'],
    #         'totalContract': brewery_types['contract'],
    #         'totalRegional': brewery_types['regional']
    #     },

           
    #     }
    jsonBrew = data.to_json(orient = "records")
    return jsonBrew
    # return data.to_json(orient = "records")
    



# class BreweryData:
#     def __init__(self, state='north_carolina')
#     self.state = state
#     self.brew_res = requests.get(f'{BASE_URL}', params={'by_state':state})
#     self.brew_res = self.brew_res.json()

#     def getBreweryByState(self):
#         breweryList = []
