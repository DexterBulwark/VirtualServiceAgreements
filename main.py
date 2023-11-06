"""
When run this file will gather all of the needed information to build and send a service agreement for a given service and location



"""
from src import get_info_from_user

if __name__ == "__main__":
    office, service = get_info_from_user()
    print(office, service)
