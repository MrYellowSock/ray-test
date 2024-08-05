import requests
import os
import json
import requests
import time

time.sleep(5)
RAY_ADDR = os.getenv('RAY_HEAD_DASHBOARD_ADDRESS')

url = f"http://{RAY_ADDR}/api/serve/applications/"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

# STORE MODELS IN GIT?
# Corrupt zip file can cause freeze?
data = {
    "applications": [
         {
            "name": "myfastapi2",
            "route_prefix": "/myfastapi2",
            "import_path": "fastapi_sample:app",
            "runtime_env": {
                # SOME HOW USING URL FOR RAW FILE DOES NOT WORK??
                "working_dir": "https://github.com/MrYellowSock/ray-test-sampleconfig/archive/refs/heads/version-pd1.zip",
                "pip":["-r ${RAY_RUNTIME_ENV_CREATE_WORKING_DIR}/requirements.txt && echo 'fastapi2'"],
            },
            "deployments": [
                {"name": "MyModelDeployment"} ]
        }
         ,{
            "name": "myfastapi",
            "route_prefix": "/myfastapi",
            "import_path": "fastapi_sample:app",
            "runtime_env": {
                # SOME HOW USING URL FOR RAW FILE DOES NOT WORK??
                "working_dir": "https://github.com/MrYellowSock/ray-test-sampleconfig/archive/refs/heads/version-pd0.zip",
                # USE VARIABLES IN WORKING_DIR
                "pip":["-r ${RAY_RUNTIME_ENV_CREATE_WORKING_DIR}/requirements.txt && echo 'fastapi'"],

            },
            "deployments": [
                {"name": "MyModelDeployment"}
            ]
        }
         ,{
            "name": "myfastapi3",
            "route_prefix": "/myfastapi3",
            "import_path": "fastapi_sample:app",
            "runtime_env": {
                # SOME HOW USING URL FOR RAW FILE DOES NOT WORK??
                "working_dir": "https://github.com/MrYellowSock/ray-test-sampleconfig/archive/refs/heads/main.zip",
                # USE VARIABLES IN WORKING_DIR
                "pip":["-r ${RAY_RUNTIME_ENV_CREATE_WORKING_DIR}/requirements.txt && echo 'fastapi3'"],

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
