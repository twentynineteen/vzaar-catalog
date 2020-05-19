from secret_key import *

import requests
import pprint

headers = {
    'X-Client-Id': api_client_id,
    'X-Auth-Token': auth_token,
}

pp = pprint.PrettyPrinter(indent=4)

def list_videos(q=''):
    '''This makes an API call to vzaar and lists all videos in account'''

    response = requests.get('https://api.vzaar.com/api/v2/videos', headers=headers)

    return response.text

def list_categories():
    '''This makes an API call to vzaar and lists all categories in account'''

    response = requests.get('https://vzaar.com/api/v2/categories', headers=headers)

    return response.text

def list_category_subtree(id):
    '''This makes an API call to vzaar and lists all categories in a given subtree'''

    response = requests.get('https://vzaar.com/api/v2/categories/' + id + '/subtree', headers=headers)

    return response.text

def lookup_category(id):
    '''This makes an API call to vzaar and looks up a category in a given id'''

    response = requests.get('https://vzaar.com/api/v2/categories/' + id, headers=headers)

    return response.text

def create_top_level_category(name):
    '''Use this to create a category on the top level of category lists.
    Reserved for programmes and qualifications.
    
    name parameter must be a string.'''

    auth_head = {
        'X-Client-Id': api_client_id,
        'X-Auth-Token': auth_token,
        'Content-Type': 'application/json',
    }

    data = '{\n       "name": \"'+name+'\"\n     }'

    response = requests.post('https://vzaar.com/api/v2/categories', headers=auth_head, data=data)
    print(response.status_code)
    if response.status_code == 201:
        print("successfully created top level category")
        print(data)
    else:
        print("command failed: see response code for more information")

def create_subcategory(name, parent_id):
    '''Use this to create a subcategory.
    Reserved for modules and year / occasion.
    
    name parameter must be a string.'''

    auth_head = {
        'X-Client-Id': api_client_id,
        'X-Auth-Token': auth_token,
        'Content-Type': 'application/json',
    }

    data = '{\n       "name": \"' + name + '\",\n       "parent_id": \"' + str(parent_id) + '\"\n     }'

    response = requests.post('https://vzaar.com/api/v2/categories', headers=auth_head, data=data)
    print(response.status_code)
    if response.status_code == 201:
        print("successfully created subcategory")
        print(data)
    else:
        print("command failed: see response code for more information")