from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import mlflow
import mlflow.pyfunc
from mlflow.exceptions import MlflowException
import config

class LLMModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2", token=config.HuggingFaceConfig.token)
        self.tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2", token=config.HuggingFaceConfig.token)

    def predict(self, context, model_input):
        input_ids = self.tokenizer(model_input, return_tensors="pt")
        outputs = self.model.generate(**input_ids, max_new_tokens=100, pad_token_id=50256)
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
experiment_name = "LLMModelExperiment"
mlflow.set_tracking_uri("http://localhost:5000")

# Ensure the experiment exists
experiment_id = get_or_create_experiment(experiment_name)
mlflow.set_experiment(experiment_id)

# Save and Register the model to MLflow
with mlflow.start_run() as run:
    mlflow.pyfunc.save_model(
        path="openai_model",
        python_model=LLMModel()
    )

    # Register the model
    try:
        mlflow.register_model(
            model_uri=f"runs:/{run.info.run_id}/openai_model",
            name="LLMModel"
        )
    except MlflowException as e:
        print(f"Error registering model: {e}")
        raise
