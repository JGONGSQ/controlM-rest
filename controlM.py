import sys
import requests
import json
from settings.local import BASE_URL, USERNAME, PASSWORD, CTM

def login(base_url=BASE_URL, username=USERNAME, password=PASSWORD):
    # define the login endpoint
    login_url = base_url + '/session/login'

    # define the headers
    headers = {'content-type': 'application/json'}

    # forming the request body
    body = {
        "username": username,
        "password": password
    }
    
    # get the response and change into the json format
    response = requests.post(login_url, json=body, headers=headers, verify=False)
    json_response = response.json()

    print("This is the login token", json_response['token'])
    return json_response['token']


def create_jobs(token, jobfile, base_url=BASE_URL):
    # define the create job endpoint
    create_job_url = base_url + '/deploy'

    # forming the file_data and headers
    file_data = {'definitionsFile': open(jobfile, 'rb')}
    headers = json.loads('{"Authorization": "Bearer ' + token + '"}')

    # post the request
    response = requests.post(create_job_url, headers=headers, files=file_data, verify=False)

    return response

def run_jobs(token, jobfile, base_url=BASE_URL):
    # define the run job endpoint
    run_job_url = base_url + '/run'

    #forming the file_data and headers
    file_data = {'jobDefinitionsFile': open(jobfile, 'rb')}
    headers = json.loads('{"Authorization": "Bearer ' + token + '"}')

    # post the run request
    response = requests.post(run_job_url, headers=headers, files=file_data, verify=False)
    return response

def run_order_jobs(token, folder, ctm_name=CTM, base_url=BASE_URL):

    run_order_job_url = base_url + '/run/order'
    body = {
        "ctm": ctm_name,
        "folder": folder
    }
    headers = json.loads('{"Authorization": "Bearer ' + token + '"}')
    response = requests.post(run_order_job_url, headers=headers, json=body, verify=False)

    return response

def main():
    
    JOB_FILE = sys.argv[1]
    print("test 123", JOB_FILE)

    # Get the login token
    token = login()

    # Create the jobs
    # response = create_jobs(token=token, jobfile=JOB_FILE)

    # response = run_jobs(token=token, jobfile=JOB_FILE)

    # print("###", response, response.text)


if __name__ == '__main__':
    main()