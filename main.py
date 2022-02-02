import sys
from clients import service_registration
from clients import service_request


def main(action, path):
    if action == "register_service":
        service_registration.register_service(path)
    if action == "register_random_service":
        service_registration.register_random_service(path)
    if action == "execute_service":
        service_request.execute_service(path)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
