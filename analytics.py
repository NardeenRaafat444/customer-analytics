import pandas as pd
import sys
import subprocess

print("Analytics started...")

# Load preprocessed dataset
dataset_path = sys.argv[1] #Gets file path from terminal.
data = pd.read_csv(dataset_path)

# -------------------------------
# Insight 1: Average income
# -------------------------------
if "Income" in data.columns: #Check if Column Exists
    avg_income = data["Income"].mean() #calc average
    insight1 = f"The average income in the dataset is {avg_income:.2f}."
else:
    insight1 = "Income column is not available for analysis."

with open("insight1.txt", "w", encoding="utf-8") as f:
    f.write(insight1)

# -------------------------------
# Insight 2: Average total spending
# -------------------------------
if "Total_Spending" in data.columns:
    avg_spending = data["Total_Spending"].mean()
    insight2 = f"The average total spending in the dataset is {avg_spending:.2f}."
else:
    insight2 = "Total_Spending column is not available for analysis."

with open("insight2.txt", "w", encoding="utf-8") as f:
    f.write(insight2)

# -------------------------------
# Insight 3: Most common education level
# -------------------------------
if "Education" in data.columns:
    top_education = data["Education_Original"].mode()[0] # mode : the most frequent first word
    insight3 = f"The most common education level in the dataset is {top_education}."
else:
    insight3 = "Education column is not available for analysis."

with open("insight3.txt", "w", encoding="utf-8") as f:
    f.write(insight3)

print("Analytics completed. Saved insight1.txt, insight2.txt, insight3.txt")

# Call next script
subprocess.run(["python", "visualize.py", dataset_path])