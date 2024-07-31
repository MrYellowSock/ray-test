import requests
import os
import json
import requests
import time

time.sleep(5)
RAY_ADDR = os.getenv('RAY_HEAD_DASHBOARD_ADDRESS')

url = f"http://{RAY_ADDR}/api/serve/applications/"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

# existing app doesn't deploy when post a new app
obj2 = {
    "applications": [
         {
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
         ,{ "name": "myfastapi2", "route_prefix": "/myfastapi2",
            "import_path": "fastapi_sample:app",
            "runtime_env": {
                # SOME HOW USING URL FOR RAW FILE DOES NOT WORK??
                "working_dir": "https://github.com/MrYellowSock/ray-test-sampleconfig/archive/HEAD.zip",
                "pip":{
                    "packages":["pandas==2.1.3"],
                }
            },
            "deployments": [
                {"name": "MyModelDeployment"}
            ]
        }
         ,
    ]
}

obj1 = {
    "applications": [
         {
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
    ]
}

ticker = True
while True:
    todeploy = obj1 if ticker else obj2
    response = requests.put(url, headers=headers, data=json.dumps(todeploy))

    ticker = not ticker
    print("DEPLOYED!")

    time.sleep(20)
    if response.status_code != 200:
        raise Exception(f"Failed to create or update application: {response.text}")
