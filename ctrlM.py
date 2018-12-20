from settings.local import BASE_URL, USERNAME, PASSWORD, CTM
from library.core import CoreAPIs 


def main():
    core_apis = CoreAPIs(USERNAME, PASSWORD, BASE_URL)
    core_apis.test()



if __name__ == '__main__':
    main()