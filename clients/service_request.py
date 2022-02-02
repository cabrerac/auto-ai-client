import requests
from util import util

base_url = 'http://127.0.0.1:5000/'


def execute_service():
    # Read request metadata
    service_request = util.read('./data/service_requests/')
    # Request service
    url = base_url + '/auto_ai/hypervisor/execute_service'
    response = requests.post(url, json=service_request)
    print(response.json())
