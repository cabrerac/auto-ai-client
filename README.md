# auto-ai-client
Client of auto-ai-doa, which can request the following functionalities at the moment:

1. Registering services.
2. Executing services.

# How to run the code

1. Requirements must be installed in the environment
```
pip install  -r requirements.txt
```

2. Run the following command in the command line on the path auto-ai-client/: 

```
$ python3 main.py "<action>" "<file_path>"
```

* action: It can be "register_service", "execute_service".
* file_path: This is the file to the service or request description.

For example to register the service described in the file service3.json:

```
python3 main.py "register_service" "./data/service_descriptions/service3.json"
```

Do both!

```
./register_services.sh && ./execute_service.sh calculate_costs_all
```
