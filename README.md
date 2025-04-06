 How it works:
Step	File	Description
1	federated_client.py	Each client trains its own model locally using only its own event_logs.csv
2	federated_server.py	Calls the client training code, collects their models, and (simplistically) chooses one or aggregates
3	-	Saves the final global_model.pkl in the models/ directory for use in detection
