#!/bin/bash

echo "Starting full pipeline..."

python ingest.py marketing_campaign.csv

echo "Pipeline finished."


#instead of 
#python ingest.py marketing_campaign.csv
#bash summary.sh
#: Run container → everything happens automatically