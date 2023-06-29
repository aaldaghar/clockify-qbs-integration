from intuitlib.enums import Scopes
import requests
import json
import Constants

#setup clockify and qbo base urls
#clockify
CLOCKIFY_BASE_URL = 'https://api.clockify.me/api/v1/'
QBO_BASE_URL =  'https://quickbooks.api.intuit.com'

def get_clockify_workspace_id():
    url ='{0}/workspaces'.format(CLOCKIFY_BASE_URL)
    response = requests.request("GET", url, headers=Constants.clockify_bearer_token)
    workspace_data = response.json()
    workspace_id = workspace_data[0]['id']
    return workspace_id



def get_clockify_recorded_hours():
    clockify_workspace_id = get_clockify_workspace_id()
    url = '{0}/workspaces/{1}/projects'.format(CLOCKIFY_BASE_URL,clockify_workspace_id)
    response = requests.request("GET", url, headers=Constants.clockify_bearer_token)
    projects_data = response.json()
    projects_hours = {}
    for project in projects_data:
        projects_hours[project['name']] = project['duration']

    return projects_hours


#qbo

#url = Constants.qbo_auth_client.get_authorization_url([Scopes.ACCOUNTING])

def create_qb_invoice():

    base_url =  'https://quickbooks.api.intuit.com'
    url = '{0}/v3/company/{1}/invoice?minorversion=65'.format(base_url, Constants.qbo_auth_client.realm_id)
    auth_header = 'Bearer {0}'.format(Constants.qbo_auth_client.access_token)
    headers = {
        'Authorization': auth_header,
        'Content-Type': 'application/json'
    }

    payload = json.dumps({
    "Line": [
        {
        "DetailType": "SalesItemLineDetail",
        "Amount": 100,
        "SalesItemLineDetail": {
            "ItemRef": {
            "name": "Services",
            "value": "1"
            }
        }
        }
    ],
    "CustomerRef": {
        "value": "1"
    }
    })

    response = requests.request("POST", url, headers=headers, data=payload)
