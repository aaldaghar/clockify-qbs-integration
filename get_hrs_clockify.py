import requests
import Constants
import datetime

#setup clockify base url
CLOCKIFY_BASE_URL = 'https://api.clockify.me/api/v1'

def get_clockify_workspace_id():
    url ='{0}/workspaces'.format(CLOCKIFY_BASE_URL)
    response = requests.request("GET", url, headers=Constants.clockify_bearer_token)
    workspace_data = response.json()
    workspace_id = workspace_data[0]['id']
    return workspace_id


def get_clockify_projects_ids():
    clockify_workspace_id = get_clockify_workspace_id()
    url = '{0}/workspaces/{1}/projects'.format(CLOCKIFY_BASE_URL,clockify_workspace_id)
    response = requests.request("GET", url, headers=Constants.clockify_bearer_token)
    projects_data = response.json()
    return projects_data

def get_clockify_billable_hours():
    clockify_workspace_id = get_clockify_workspace_id()
    clockify_projects_id = get_clockify_projects_ids()
    url = '{0}/workspaces/{1}/user/{2}/time-entries'.format(CLOCKIFY_BASE_URL,clockify_workspace_id, clockify_projects_id[0]['memberships'][0]['userId'])
    response = requests.request("GET", url, headers=Constants.clockify_bearer_token)
    time_entries_data = response.json()
    qb_hours = {}
    for time in time_entries_data:
       for projects in clockify_projects_id:
          if time['projectId'] == projects['id']:
             start_date = datetime.datetime.strptime(time['timeInterval']['start'],"%Y-%m-%dT%H:%M:%SZ")
             end_date = datetime.datetime.strptime(time['timeInterval']['end'],"%Y-%m-%dT%H:%M:%SZ")
             total_hours = end_date - start_date
             billable_hours = str(datetime.timedelta(seconds=total_hours.seconds))
             qb_hours_str = billable_hours.split(':',1)[0]
             qb_hours_int = int(qb_hours_str)
             if projects['name'] not in qb_hours:
                qb_hours[projects['name']] = qb_hours_int
             else:
                qb_hours[projects['name']] += qb_hours_int
    return qb_hours