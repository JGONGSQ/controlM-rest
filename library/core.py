import sys
import requests
import json


class CoreAPIs(object):

    def __init__(self, username, password, base_url):
        self.username = username
        self.password = password
        self.base_url = base_url
        self.headers = {'content-type': 'application/json'}
        self.token = self.login(username, password, base_url)
        

    def login(self, username, password, base_url):
        
        login_url = base_url + '/session/login'

        body = {
            "username": username,
            "password": password
        }

        response = requests.post(login_url, headers=self.headers, json=body, verify=False)
        
        return response.json()['token']

    def test(self):
        print("This is the token", self.token)
        return