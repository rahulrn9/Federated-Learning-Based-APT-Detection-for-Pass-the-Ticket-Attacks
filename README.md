# Federated-Learning-Based-APT-Detection-for-Pass-the-Ticket-Attacks
A security-focused machine learning system using Federated Learning to detect Pass-the-Ticket (PtT) attacks as described in MITRE ATT&CK T1550.003. The project simulates a multi-client environment where models are trained locally on sensitive ticket log data and aggregated centrally — without sharing raw data.

Features
 Federated Learning simulation with local training per client

 Central aggregation of models (FedAvg-style)

 Detection of anomalous Kerberos ticket behaviors

 Simulated log data representing real-world PtT attack patterns

 CI/CD + DevSecOps via GitHub Actions

 Dockerized & testable

  How It Works
Each client (e.g., client1, client2) loads and trains a model on its local Kerberos event logs.

Local models are then aggregated centrally by the FL server using basic averaging or any chosen strategy.

A global model is produced that can detect anomalous ticket behavior (e.g., abnormally large ticket size, frequent reuse).

Predictions can be run on new logs using the saved model.

🛠️ Setup
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/Federated-APT-Detection.git
cd Federated-APT-Detection
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Verify Data

Ensure there are CSV files like data/client1/event_logs.csv, data/client2/event_logs.csv, etc.

🏃 Run the Project
🏁 Train Federated Global Model
bash
Copy
Edit
python federated/federated_server.py
🔍 Analyze New Log
bash
Copy
Edit
python detection/ticket_analyzer.py
📊 Sample Data
Each client log (event_logs.csv) contains:

src_ip	dst_ip	ticket_size	validity	logon_count	label
192.168.1.10	192.168.1.20	550	86400	3	0
192.168.1.10	192.168.1.25	5000	86400	2	1
label = 1 denotes suspected Pass-the-Ticket activity.

🔐 DevSecOps Integration
CI pipeline using GitHub Actions:

✅ Code linting

✅ Pytest for unit tests

✅ Bandit for static security checks

✅ Gitleaks for secrets scanning

yaml
Copy
Edit
.github/workflows/ci-devsecops.yml
To trigger:

bash
Copy
Edit
git push origin main
🧪 Testing
bash
Copy
Edit
pytest tests/
📦 Docker Support
Build the Image
bash
Copy
Edit
docker build -t federated-detector .
Run the App
bash
Copy
Edit
docker run -v $(pwd):/app federated-detector
📈 Future Work
. Add real FedAvg model weight aggregation

. Extend to 10+ clients with dynamic orchestration

.Integrate LSTM/AutoEncoders for better anomaly detection

. Add Streamlit dashboard for real-time detection results

