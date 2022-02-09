import json
import random
import os


def read_random(path):
    file_name = random.choice(os.listdir(path))
    service_path = os.path.join(path, file_name)
    f = open(service_path)
    service_description = json.load(f)
    f.close()
    return service_description


def read_file(file_name):
    f = open(file_name)
    service_description = json.load(f)
    f.close()
    return service_description
