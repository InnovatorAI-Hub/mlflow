# mlflow

## run mlflow server for registory:
```sh
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns/ --host 127.0.0.1 --port 5000

```