from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import mlflow
import mlflow.pyfunc
from mlflow.exceptions import MlflowException

class GemmaMLflow(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        quantization_config = BitsAndBytesConfig(load_in_8bit=True)
        self.model = AutoModelForCausalLM.from_pretrained("google/gemma-2b", quantization_config=quantization_config, device_map="auto")
        self.tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")

    def predict(self, context, model_input):
        input_ids = self.tokenizer(model_input, return_tensors="pt").to("cuda")
        outputs = self.model.generate(**input_ids)
        return self.tokenizer.decode(outputs[0])

def get_or_create_experiment(experiment_name):
    try:
        experiment = mlflow.get_experiment_by_name(experiment_name)
        if experiment is None:
            experiment_id = mlflow.create_experiment(experiment_name)
        else:
            experiment_id = experiment.experiment_id
        return experiment_id
    except MlflowException as e:
        print(f"Error getting or creating experiment: {e}")
        raise

# Configuration
experiment_name = "GemmaMLflowExperiment"
mlflow.set_tracking_uri("http://localhost:5000")

# Ensure the experiment exists
experiment_id = get_or_create_experiment(experiment_name)
mlflow.set_experiment(experiment_id)

# Save and Register the model to MLflow
with mlflow.start_run() as run:
    mlflow.pyfunc.save_model(
        path="gemma_model",
        python_model=GemmaMLflow()
    )

    # Register the model
    try:
        mlflow.register_model(
            model_uri=f"runs:/{run.info.run_id}/gemma_model",
            name="GemmaMLflow"
        )
    except MlflowException as e:
        print(f"Error registering model: {e}")
        raise
