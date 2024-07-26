import requests
from starlette.requests import Request
from typing import Dict
from ray import serve

@serve.deployment
class MyModelDeployment:
    def __init__(self, msg: str):

        self._msg = msg

    def __call__(self, request: Request) -> Dict:
        import os
        import pandas as pd
        return {
                "result": self._msg,
                "hostname": os.uname()[1],
                "version":pd.__version__
        }

app = MyModelDeployment.bind(msg="Hello world!")
