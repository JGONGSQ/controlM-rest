import sys
import argparse
import json
from settings.local import BASE_URL, USERNAME, PASSWORD
from library.core import CoreAPIs 


def main():
    action_str = 'action'
    authentication_str = 'auth'
    extra_var_str = 'extra_var'

    parser = argparse.ArgumentParser(
        description="Start of the ControlM REST API package"
        )
    parser.add_argument(action_str, help="The action take for the script, e.g. deploy or run")
    parser.add_argument("-"+authentication_str, nargs="?", help='The authentication dict including {"username":"username", "password":"password", "base_url":"base_url"}')    
    parser.add_argument("-"+extra_var_str, nargs="?", help="The extra parameters would be needed for the action, could be a filepath or extra extra variables")
    args = parser.parse_args()

    authentication_json = getattr(args, authentication_str)
    if not authentication_json:
        core_apis = CoreAPIs(USERNAME, PASSWORD, BASE_URL)
    else:
        auth_dict = json.loads(authentication_json)
        core_apis = CoreAPIs(auth_dict['username'], auth_dict['password'], auth_dict['base_url'])

    # login to the system
    if args.action == 'login':
        response = core_apis.login()

    # deploy jobs
    if args.action == 'deploy': 
        job_file = getattr(args, extra_var_str)
        response = core_apis.deploy_jobs(job_file)

    # run order the jobs
    if args.action == 'run':
        extra_var = getattr(args, extra_var_str)
        if not extra_var:
            extra_var = {"orderDate": "20181212"}

        response = core_apis.run_order_jobs(
            kwargs=extra_var)
    
    print("This is the response", response, response.text)
    return


if __name__ == '__main__':
    main()