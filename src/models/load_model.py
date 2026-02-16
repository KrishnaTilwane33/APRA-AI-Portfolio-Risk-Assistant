import joblib

def load_model(path="outputs/model.joblib"):
    model = joblib.load(path)

    print(f"📦 Model loaded <-- {path}")

    return model