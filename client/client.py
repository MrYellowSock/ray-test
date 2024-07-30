import requests
import os
import time
from fastapi import FastAPI
from typing import Dict
from ray import serve
import ray

time.sleep(5)
RAY_ADDR = os.getenv('RAY_HEAD_CLIENT_CONNECT_ADDRESS')

ray.init(
        address=f"ray://{RAY_ADDR}",
        runtime_env={
            "pip":{
                # Changes this around
                "packages":["pandas==2.2.1"]
            }
        }
)

app = FastAPI()
@serve.deployment
@serve.ingress(app)
class MyModelDeployment:
    def __init__(self, msg: str):

        self._msg = msg

    @app.get("/")
    def root(self) -> Dict:
        import os
        import pandas as pd
        return {"result": self._msg, "hostname": os.uname()[1], "pd_version":pd.__version__}

    @app.post("/ping")
    def ping(self,name:str) -> Dict:
        return {"result": f"pong {name}"}

serve.start(detached=True, http_options={"host": "0.0.0.0"})  # Start the Ray Serve instance
serve.run(MyModelDeployment.bind(msg="Hello world!"), route_prefix="/")


print(requests.get(f"http://{os.getenv('RAY_HOST')}:8000/").json())
# {'result': 'Hello world!', 'hostname': 'xxx', 'version': '2.2.1'}
