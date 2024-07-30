from fastapi import FastAPI
from typing import Dict
from ray import serve

api = FastAPI()
@serve.deployment
@serve.ingress(api)
class MyModelDeployment:
    def __init__(self, msg: str):

        self._msg = msg

    @api.get("/")
    def root(self) -> Dict:
        import os
        import pandas as pd
        return {"result": self._msg, "hostname": os.uname()[1], "pd_version":pd.__version__}

    @api.post("/ping")
    def ping(self,name:str) -> Dict:
        return {"result": f"pong {name}"}
app = MyModelDeployment.bind(msg="Hello world!")
