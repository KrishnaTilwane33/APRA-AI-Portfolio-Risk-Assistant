import joblib
from pathlib import Path

def save_model(model,path='outputs/model.joblib'):
    Path('outputs').mkdir(exist_ok=True)
    joblib.dump(model, path)
    print(f'💾 Model saved --> {path}')