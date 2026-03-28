import pandas as pd
import sys
#sys is a built-in Python module that lets your program interact with the system, especially the command line and Python runtime.

# Step 1: Get dataset path from command line
dataset_path = sys.argv[1]

# Step 2: Load dataset
data = pd.read_csv(dataset_path, sep="\t")
# Step 3: Save raw copy
data.to_csv("data_raw.csv", index=False) #Do NOT save the row numbers (index) into the CSV file.

print("Data ingestion completed. Raw data saved as data_raw.csv")

# Step 4: Call next script, Run another Python file automatically from inside this script.
import subprocess # python module lets python Run other programs from inside Python
subprocess.run(["python", "preprocess.py", "data_raw.csv"])
#Run this command: python preprocess.py data_raw.csv like in terminal