import requests
import json

from settings.local import CTM, TEST_FOLDER


class CoreAPIs(object):

    def __init__(self, username, password, base_url):
        self.username = username
        self.password = password
        self.base_url = base_url
        self.headers = {'content-type': 'application/json'}
        self.token = self.login(username, password, base_url)
        self.auth_headers = {"Authorization": "Bearer " + self.token}
        

    def login(self, username, password, base_url):
        # define the login url
        login_url = base_url + '/session/login'

        body = {
            "username": username,
            "password": password
        }

        response = requests.post(login_url, headers=self.headers, json=body, verify=False)
        
        return response.json()['token']

    def deploy_jobs(self, jobfile):
        # define the deploy job url
        deploy_job_url = self.base_url + '/deploy'

        # forming the file_data
        file_data = file_data = {'definitionsFile': open(jobfile, 'rb')}

        response = requests.post(deploy_job_url, headers=self.auth_headers, files=file_data, verify=False)
        return response

    def run_order_jobs(self, ctm=CTM, folder=TEST_FOLDER, **kwargs):
        # define the run order url
        run_order_job_url = self.base_url + '/run/order'

        body = {
            "ctm": ctm,
            "folder": folder
        }

        orderDate_key = 'orderDate'
        if 'kwargs' in kwargs:
            orderDate = kwargs['kwargs'].get(orderDate_key)
            # updates the body dict
            body.update({orderDate_key: orderDate})
        
        response = requests.post(run_order_job_url, headers=self.auth_headers, json=body, verify=False)
        
        return response
        

