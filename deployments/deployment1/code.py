from fastapi import FastAPI
from typing import Dict
from ray import serve

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

