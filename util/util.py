import json
import random
import os


def read(path):
    filename = random.choice(os.listdir(path))
    service_path = os.path.join(path, filename)
    f = open(service_path)
    service_description = json.load(f)
    f.close()
    return service_description
