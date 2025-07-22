import os
from src.model import train

def test_train_model():
    train.train_model()
    assert os.path.exists("model.joblib")
    print("✅ test_train_model passed")
