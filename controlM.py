import sys
import requests
import json

BASE_URL = "https://localhost:8443/automation-api"

def login(base_url=BASE_URL, username="workbench", password="workbench"):
    # define the login endpoint
    login_url = base_url + '/session/login'

    # forming the request body and headers
    body = {"password": password, "username": username}
    headers = {'content-type': 'application/json'}
    
    # get the response and change into the json format
    response = requests.post(login_url, json=body, verify=False, headers=headers)
    json_response = response.json()

    print("This is the login token", json_response['token'])
    return json_response['token']


def create_jobs(token, jobfile, base_url=BASE_URL):
    # define the create job endpoint
    create_job_url = base_url + '/deploy'

    file_data = {'definitionsFile': open(jobfile, 'rb')}
    headers = json.loads('{"Authorization": "Bearer ' + token + '"}')
    # print("This is the header data", headers)

    response = requests.post(create_job_url, headers=headers, files=file_data, verify=False)

    return response


def main():
    
    JOB_FILE = sys.argv[1]
    print("test 123", JOB_FILE)

    # Get the login token
    token = login()

    # Create the jobs
    response = create_jobs(token=token, jobfile=JOB_FILE)

    print("###", response, response.text)


if __name__ == '__main__':
    main()