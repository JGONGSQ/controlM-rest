import sys
import argparse

from settings.local import BASE_URL, USERNAME, PASSWORD, CTM
from library.core import CoreAPIs 


def main():
    extra_var_str = 'extra-var'
    action_str = 'action'

    parser = argparse.ArgumentParser(
        description="Start of the ControlM REST API package"
        )
    parser.add_argument(action_str, help="The action take for the script, e.g. deploy or run")
    parser.add_argument(extra_var_str, nargs="?", help="The extra parameters would be needed for the action, could be a filepath or extra extra variables")
    args = parser.parse_args()

    core_apis = CoreAPIs(USERNAME, PASSWORD, BASE_URL)

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