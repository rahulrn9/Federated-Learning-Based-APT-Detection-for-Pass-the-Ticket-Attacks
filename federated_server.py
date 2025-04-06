import os
from federated.federated_client import train_local_model
from models.global_model import GlobalModel
import joblib

def aggregate_models(local_models):
    """
    Basic placeholder for aggregation — picks the first model.
    In real federated learning, you'd average model weights (e.g., FedAvg).
    """
    print("[!] Aggregating models — using first model as global (simplified).")
    return local_models[0]

def federated_training():
    client_dirs = ["data/client1", "data/client2"]  # Can expand to more clients
    
    local_models = []
    for client_dir in client_dirs:
        model = train_local_model(client_dir)
        local_models.append(model)
    
    global_model = aggregate_models(local_models)
    global_model.save()
    print("[✓] Federated training complete. Global model saved to models/global_model.pkl")

if __name__ == "__main__":
    federated_training()
