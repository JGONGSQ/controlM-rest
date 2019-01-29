import requests
import json

from settings.local import CTM, TEST_FOLDER


class CoreAPIs(object):

    def __init__(self, username, password, base_url):
        self.username = username
        self.password = password
        self.base_url = base_url
        self.headers = {'content-type': 'application/json'}
        self.token = self.login().json()['token']
        self.auth_headers = {"Authorization": "Bearer " + self.token}
        

    def login(self):
        # define the login url
        login_url = self.base_url + '/session/login'

        body = {
            "username": self.username,
            "password": self.password
        }

        response = requests.post(login_url, headers=self.headers, json=body, verify=False)
        return response

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

        if 'kwargs' in kwargs:
            # updates the body dict
            for k, v in kwargs['kwargs'].items():
                body.update({k: v})

        response = requests.post(run_order_job_url, headers=self.auth_headers, json=body, verify=False)
        return response

    def run_jobs_get_status(self, **kwargs):
        # define the run jobs get status url
        run_jobs_get_status_url = self.base_url + '/run/jobs/status'
        body = dict()

        if 'kwargs' in kwargs:
            # update the body dict
            for k, v in kwargs['kwargs'].items():
                body.update({k: v})

        response = requests.get(run_jobs_get_status_url, headers=self.auth_headers, params=body, verify=False)
        return response

    def run_job_status(self, job_id):
        run_job_status_url = self.base_url + '/run/job/{job_id}/status'.format(job_id=job_id)

        # make the get call
        response = requests.get(run_job_status_url, headers=self.headers, verify=False)
        return response

    def rerun_job(self, job_id):
        # define the re-run jobs url
        rerun_job_url = self.base_url + '/run/job/{job_id}/rerun'.format(job_id=job_id)
        
        # make the post call
        response = requests.post(rerun_job_url, headers=self.headers, verify=False)
        return response
        

