from mlflow import log_metric, log_param, log_artifact
import mlflow

if __name__ == "__main__":

    mlflow.set_tracking_uri('http://localhost:5000')

    log_param("threshold", 3)
    log_param("verbosity", "DEBUG")

    log_metric("timestamp", 1000)
    log_metric("TTC", 33)

    log_artifact("/workspaces/mlflow/data_file.csv")