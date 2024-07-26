import pandas as pd
from fastapi import FastAPI
from ray import serve
import io

# 1: Define a FastAPI app and wrap it in a deployment with a route handler.
app = FastAPI()


@serve.deployment(
    name="deployment1",
    num_replicas=2,
    ray_actor_options={"num_cpus": 2, "num_gpus": 0},
    max_ongoing_requests=100,
    health_check_period_s=10,
    health_check_timeout_s=30,
    graceful_shutdown_timeout_s=20,
    graceful_shutdown_wait_loop_s=2,
)
@serve.ingress(app)
class FastAPIDeployment:
    def __init__(self):
        # get bigmodel file size
        with open("deployment1/bigmodel.pkl", "rb") as f:
            self.bigmodel = io.BytesIO(f.read())

    # FastAPI will automatically parse the HTTP request for us.
    @app.get("/hello")
    def say_hello(self, name: str) -> str:
        return f"Hello {name}! with {pd.__version__} {self.bigmodel.getbuffer().nbytes}"

