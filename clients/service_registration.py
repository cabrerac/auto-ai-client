import requests
from util import util

base_url = 'http://127.0.0.1:5000/'


def register_service():
    # Read service metadata
    service_description = util.read('./data/service_descriptions/')
    # Build service image
    # Push service image
    # Request service registration
    url = base_url + '/auto_ai/hypervisor/register_service'
    response = requests.post(url, json=service_description)
    print(response.json())


def register_services(n):
    for i in range(n):
        register_service()
