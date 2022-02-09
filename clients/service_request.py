import requests
from util import util

base_url = 'http://127.0.0.1:5000/'


def execute_random_service(path):
    # Read request metadata
    service_request = util.read_random(path)
    # Request service
    url = base_url + '/auto_ai/hypervisor/execute_service'
    response = requests.post(url, json=service_request)
    print(response.json())


def execute_service(file_name):
    # Read request metadata
    service_request = util.read_file(file_name)
    # Request service
    url = base_url + '/auto_ai/hypervisor/execute_service'
    response = requests.post(url, json=service_request)
    print(response.json())
