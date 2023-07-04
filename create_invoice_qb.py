#import Constants
import json
import requests
import get_hrs_clockify
import logging

#logger
logger = logging.getLogger('qb_invoice')
# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)
# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

#setup qbo base url
QBO_BASE_URL =  'https://quickbooks.api.intuit.com'


def create_qb_invoice():
    hours = get_hrs_clockify.get_clockify_billable_hours()
    url = '{0}/v3/company/{1}/invoice?minorversion=65'.format(QBO_BASE_URL, qbo_auth_client.realm_id)
    auth_header = 'Bearer {0}'.format(qbo_auth_client.access_token)
    headers = {
        'Authorization': auth_header,
        'Content-Type': 'application/json'
    }
    list_hours = sorted(list(hours.items()))
    payload = json.dumps({
        "Line": [
        {
         "Id": "1",
         "LineNum": 1,
         "Amount": list_hours[0][1]*107,
         "DetailType": "SalesItemLineDetail",
         "SalesItemLineDetail": {
          "ItemRef": {
           "value": "19",
           "name": list_hours[0][0]
          },
          "UnitPrice": 107,
          "Qty": list_hours[0][1],
          "ItemAccountRef": {
           "value": "5",
           "name": "Services"
          }
         }
        },
        {
         "Id": "2",
         "LineNum": 2,
         "Amount": list_hours[1][1]*107,
         "DetailType": "SalesItemLineDetail",
         "SalesItemLineDetail": {
          "ItemRef": {
           "value": "20",
           "name": list_hours[1][0]
          },
          "UnitPrice": 107,
          "Qty": list_hours[1][1],
          "ItemAccountRef": {
           "value": "5",
           "name": "Services"
          }
         }
        },
        {
         "Id": "3",
         "LineNum": 3,
         "Amount": list_hours[3][1]*107,
         "DetailType": "SalesItemLineDetail",
         "SalesItemLineDetail": {
          "ItemRef": {
           "value": "21",
           "name": list_hours[3][0]
          },
          "UnitPrice": 107,
          "Qty": list_hours[3][1],
          "ItemAccountRef": {
           "value": "5",
           "name": "Services"
          },
         }
        },
        {
         "Id": "4",
         "LineNum": 4,
         "Amount": list_hours[2][1]*107,
         "DetailType": "SalesItemLineDetail",
         "SalesItemLineDetail": {
          "ItemRef": {
           "value": "22",
           "name": list_hours[2][0]
          },
          "UnitPrice": 107,
          "Qty": list_hours[2][1],
          "ItemAccountRef": {
           "value": "5",
           "name": "Services"
          },
         }
        }, 
       ],
        "CustomerRef": {
        "value": "4",
        "name": "Lawrence Berkeley National Laboratory"
       },
        "CustomerMemo": {
        "value": "Please contact us at asma.samano@protonmail.com for any questions."
       },
        "BillAddr": {
        "Id": "30",
        "Line1": "Lawrence Berkeley National Laboratory",
        "Line2": "1 Cyclotron Rd.",
        "Line3": "Berkeley, CA  94720 USA"
       },
        "ShipAddr": {
        "Id": "31",
        "Line1": "Lawrence Berkeley National Laboratory",
        "Line2": "1 Cyclotron Rd.",
        "Line3": "Berkeley, CA  94720 USA"
       },
        "ShipFromAddr": {
        "Id": "32",
        "Line1": "null"
       },
       "SalesTermRef": {
        "value": "2",
        "name": "Net 15"
       },
       })
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code != 200:
        logger.error(f'{response.status_code} ERROR')

