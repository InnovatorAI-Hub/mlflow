from  mlflow import log_metric
from random import choice
import mlflow

metric_name = ["cpu", "ram", "disk"]
percentage = [i for i in range(0, 100)]

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment(experiment_id="958214374375129121")

for i in range(40):
    log_metric(choice(metric_name), choice(percentage))