FROM python:3.10

# Install MLflow
RUN pip install mlflow

# Set the working directory
WORKDIR /app

# Expose the MLflow server port
EXPOSE 5000

# Run the MLflow server with the specified backend store URI and default artifact root
CMD mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns