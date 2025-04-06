import argparse
import pandas as pd
from models.global_model import GlobalModel
from models.utils import load_data

def analyze_tickets(input_csv):
    """
    Loads new ticket data and uses the global model to predict anomalies.
    """
    print(f"[•] Loading global model...")
    model = GlobalModel()
    model.load()  # loads from models/global_model.pkl

    print(f"[•] Loading input data from {input_csv}...")
    X, _ = load_data(input_csv)  # Label not required for prediction

    print("[•] Running predictions...")
    predictions = model.predict(X)

    results = pd.read_csv(input_csv)
    results["prediction"] = predictions
    results["prediction_label"] = results["prediction"].map({0: "Normal", 1: "Suspicious"})

    print("\n📊 Detection Results:")
    print(results[["src_ip", "dst_ip", "ticket_size", "logon_count", "prediction_label"]])
    
    # Optional: Save results
    output_path = input_csv.replace(".csv", "_analyzed.csv")
    results.to_csv(output_path, index=False)
    print(f"\n[✓] Analysis complete. Results saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_csv", type=str, required=True, help="Path to CSV file with ticket logs to analyze")
    args = parser.parse_args()

    analyze_tickets(args.input_csv)
