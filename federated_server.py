import os
import argparse
from models.client_model import ClientModel
from models.utils import load_data

def train_local_model(client_dir):
    """
    Trains a local model using the client's log data.
    """
    data_path = os.path.join(client_dir, "event_logs.csv")
    X, y = load_data(data_path)
    
    model = ClientModel()
    model.train(X, y)
    
    print(f"[✓] Trained local model for {client_dir}")
    return model

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--client_dir", type=str, required=True, help="Path to client data folder (e.g., data/client1)")
    args = parser.parse_args()
    
    train_local_model(args.client_dir)
