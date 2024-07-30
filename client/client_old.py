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
            "name": "sleep1",
            "route_prefix": "/sleep1",
            "import_path": "sleepy_pid:app",
            "runtime_env": {
                "working_dir": "s3://wahthecufk/ray-test-sampleconfig-997702ffa1315db0f5c9c679d8d6a2f9f43c7b63.zip"
            },
            "deployments": [
                {"name": "SleepyPid"}
            ]
        }
         ,{
            "name": "sleep2",
            "route_prefix": "/sleep2",
            "import_path": "sleepy_pid:app",
            "runtime_env": {
                # SOME HOW USING URL FOR RAW FILE DOES NOT WORK??
                "working_dir": "https://github.com/MrYellowSock/ray-test-sampleconfig/archive/HEAD.zip"
            },
            "deployments": [
                {"name": "SleepyPid"}
            ]
        }
         ,{
            "name": "myfastapi",
            "route_prefix": "/myfastapi",
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
