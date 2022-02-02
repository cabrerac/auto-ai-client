import requests
from util import util

base_url = 'http://127.0.0.1:5000/'


def register_random_service(services_path):
    # Read service metadata
    service_description = util.read_random(services_path)
    # Build service image
    # Push service image
    # Request service registration
    url = base_url + '/auto_ai/hypervisor/register_service'
    response = requests.post(url, json=service_description)
    print(response.json())


def register_service(file_name):
    # Read service metadata
    service_description = util.read_file(+file_name)
    # Build service image
    # Push service image
    # Request service registration
    url = base_url + '/auto_ai/hypervisor/register_service'
    response = requests.post(url, json=service_description)
    print(response.json())


def register_services(n, services_path):
    for i in range(n):
        register_random_service(services_path)
