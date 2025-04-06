import os
from federated.federated_client import train_local_model
from models.global_model import GlobalModel
from models.utils import load_data

def test_local_model_training():
    model = train_local_model("data/client1")
    assert model is not None
    assert hasattr(model, "model")

def test_global_model_load_save():
    model = GlobalModel()
    X, y = load_data("data/client1/event_logs.csv")
    model.train(X, y)
    model.save("models/test_model.pkl")

    new_model = GlobalModel()
    new_model.load("models/test_model.pkl")
    preds = new_model.predict(X)
    assert len(preds) == len(y)
