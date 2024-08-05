import requests
import os
import json
import requests
import time

time.sleep(5)
RAY_ADDR = os.getenv('RAY_HEAD_DASHBOARD_ADDRESS')

url = f"http://{RAY_ADDR}/api/serve/applications/"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

data = {
    "applications": [
         {
            "name": "regular_composite",
            "route_prefix": "/regular_composite",
            "import_path": "regular_composite:app",
            "runtime_env": {
                # SOME HOW USING URL FOR RAW FILE DOES NOT WORK??
                "working_dir": "https://github.com/MrYellowSock/ray-test-sampleconfig/archive/HEAD.zip"
            },
            "deployments": [
                {"name": "Ingress"}
            ]
        },
         {
            "name": "fastapi_composite",
            "route_prefix": "/fastapi_composite",
            "import_path": "fastapi_composite:ingress_fastapi",
            "runtime_env": {
                "working_dir": "https://github.com/MrYellowSock/ray-test-sampleconfig/archive/HEAD.zip"
            },
            "deployments": [
                {"name": "IngressFastAPI"}
            ]
        },
         {
            "name": "fastapi_composite2",
            "route_prefix": "/fastapi_composite2",
            "import_path": "fastapi_composite2:ingress",
            "runtime_env": {
                "working_dir": "https://github.com/MrYellowSock/ray-test-sampleconfig/archive/HEAD.zip"
            },
            "deployments": [
                {"name": "Adder"},
                {"name": "Multiplier"},
                {"name": "Ingress"},
            ]
        }

         ,{
            "name": "fastapi_sample",
            "route_prefix": "/fastapi_sample",
            "import_path": "fastapi_sample:app",
            "runtime_env": {
                # SOME HOW USING URL FOR RAW FILE DOES NOT WORK??
                "working_dir": "https://github.com/MrYellowSock/ray-test-sampleconfig/archive/HEAD.zip"
            },
            "deployments": [
                {"name": "MyModelDeployment"}
            ]
        }
    ]
}


response = requests.put(url, headers=headers, data=json.dumps(data))

if response.status_code != 200:
    raise Exception(f"Failed to create or update application: {response.text}")
print("DEPLOYED")
