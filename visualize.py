import pandas as pd
import sys
import subprocess
import matplotlib.pyplot as plt

print("Visualization started...")

# Load preprocessed dataset
dataset_path = sys.argv[1]
data = pd.read_csv(dataset_path)

# Create one figure with 3 plots
plt.figure(figsize=(18, 5))

# -------------------------------
# Plot 1: Age distribution
# -------------------------------

plt.subplot(1, 3, 1)
if "Age" in data.columns:
    plt.hist(data["Age"], bins=20)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
else:
    plt.text(0.5, 0.5, "Age column not found", ha="center", va="center")
    plt.title("Age Distribution")

# -------------------------------
# Plot 2: Income vs Total Spending
# -------------------------------

plt.subplot(1, 3, 2)
if "Income" in data.columns and "Total_Spending" in data.columns:
    plt.scatter(data["Income"], data["Total_Spending"])
    plt.title("Income vs Total Spending")
    plt.xlabel("Income")
    plt.ylabel("Total Spending")
else:
    plt.text(0.5, 0.5, "Income / Total_Spending not found", ha="center", va="center")
    plt.title("Income vs Total Spending")

# -------------------------------
# Plot 3: Education count
# -------------------------------

plt.subplot(1, 3, 3)
if "Education" in data.columns:
    data["Education"].value_counts().plot(kind="bar")
    plt.title("Education Levels")
    plt.xlabel("Education")
    plt.ylabel("Count")
else:
    plt.text(0.5, 0.5, "Education column not found", ha="center", va="center")
    plt.title("Education Levels")

plt.tight_layout()
plt.savefig("summary_plot.png")
plt.close()

print("Visualization completed. Saved as summary_plot.png")

# Call next script
subprocess.run(["python", "cluster.py", dataset_path])