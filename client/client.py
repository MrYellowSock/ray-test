import requests
import os
import json
import requests
import time

time.sleep(5)

RAY_ADDR = os.getenv('RAY_HEAD_DASHBOARD_ADDRESS')
FILE_SERVER_ADDR = os.getenv('FILE_SERVER_ADDRESS')

url = f"http://{RAY_ADDR}/api/serve/applications/"
headers = {"Accept": "application/json", "Content-Type": "application/json"}


data ={
    "applications": [
        {
            "name": "deployment1",
            "route_prefix": "/",
            "import_path": "code:app",
            "runtime_env": {
                # "working_dir": "https://github.com/ray-project/serve_config_examples-master.zip"
                # "working_dir": "s3://tisco.alpha.data.analytics/test_ray_working_dir/test.zip",
                # "working_dir": f"file://{os.path.abspath('text_ml.zip')}"
                "working_dir": f"http://{FILE_SERVER_ADDR}/deployment1/deployment1.zip",
                "pip":[ "-r" ,"requirements.txt" ] 
            },
            "deployments": [
                {"name": "deployment1"},
            ]
        },
    ]
}

response = requests.put(url, headers=headers, data=json.dumps(data))

if response.status_code != 200:
    raise Exception(f"Failed to create or update application: {response.text}")
