Input Format
The tool expects a CSV with the following columns:

Column	Type	Description
src_ip	string	Source IP of the user/system
dst_ip	string	Destination IP (e.g., KDC or service)
ticket_size	integer	Size of the Kerberos ticket
validity	integer	Duration in seconds the ticket is valid
logon_count	integer	Number of logon attempts using the ticket
label	integer	Optional (ignored)
If label is present, it is not used in prediction but retained for evaluation purposes.

 Usage
 Step 1: Ensure the Global Model Exists
Make sure you've already run:

bash
Copy
Edit
python federated/federated_server.py
This will save the global model to models/global_model.pkl.

 Step 2: Run the Analyzer
bash
Copy
Edit
python detection/ticket_analyzer.py --input_csv new_logs.csv
 Output
Console output showing predictions (Normal or Suspicious)

A new file: new_logs_analyzed.csv containing the results

Example output in new_logs_analyzed.csv:

src_ip	dst_ip	ticket_size	...	prediction	prediction_label
10.0.0.10	10.0.0.20	500	...	0	Normal
10.0.0.12	10.0.0.25	6000	...	1	Suspicious
