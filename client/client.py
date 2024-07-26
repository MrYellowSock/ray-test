import requests
import os
import json
import requests
import time

time.sleep(5)
RAY_ADDR = os.getenv('RAY_HEAD_DASHBOARD_ADDRESS')

url = f"http://{RAY_ADDR}/api/serve/applications/"
headers = {"Accept": "application/json", "Content-Type": "application/json"}


data ={
    "applications": [
        {
            "name": "my_model_app",
            "route_prefix": "/my_model",
            "deployments": [
                {
                    "name": "MyModelDeployment",
                    "import_path": "code.MyModelDeployment",
                    "init_args": {"msg": "Hello world!"},
                    "num_replicas": 1,
                    "route_prefix": "/"
                }
            ]
        }
    ]
}

response = requests.put(url, headers=headers, data=json.dumps(data))

if response.status_code != 200:
    raise Exception(f"Failed to create or update application: {response.text}")
print("DEPLOYED")
