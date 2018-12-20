import sys

from settings.local import BASE_URL, USERNAME, PASSWORD, CTM
from library.core import CoreAPIs 


def main():
    core_apis = CoreAPIs(USERNAME, PASSWORD, BASE_URL)

    # Sample calls
    # deploy jobs
    if sys.argv.__len__() > 1:
        job_file = sys.argv[1]
        response = core_apis.deploy_jobs(job_file)

    # test run order the jobs
    response = core_apis.run_order_jobs(kwargs={"orderDate": "20181212"})

    # response = core_apis.run_order_jobs()
    
    print("This is the response", response, response.text)


if __name__ == '__main__':
    main()