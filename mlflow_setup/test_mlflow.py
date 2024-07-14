import mlflow.pyfunc
import mlflow

# Configuration
mlflow.set_tracking_uri("http://localhost:5000") 
model_name = "openai_model"  

def load_model():
    # Load the registered model
    model = mlflow.pyfunc.load_model(model_name)
    return model


if __name__ == "__main__":
    # Load the model
    gemma_model = load_model()

    # Example text input
    input_text = "Example input for inference."

    # Perform inference
    result = gemma_model.predict(input_text)
    print("Generated text:", result)
    result = gemma_model.predict(input_text)
    print("Generated text:", result)
