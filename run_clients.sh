#!/bin/bash

for client_dir in data/client1 data/client2; do
    echo "[•] Training local model for $client_dir"
    python federated/federated_client.py --client_dir $client_dir
done
