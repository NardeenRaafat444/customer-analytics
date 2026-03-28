import sys
import pandas as pd
import numpy as np
import subprocess
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA

# Step 1: Read input file path
input_file = sys.argv[1]

# Step 2: Load data
data = pd.read_csv(input_file)

print("Preprocessing started...")
print("Original shape:", data.shape)

# =========================
# A) DATA CLEANING
# =========================

# 1. Remove duplicates
data = data.drop_duplicates()

# 2. Handle missing values in Income
data["Income"] = data["Income"].fillna(data["Income"].median())

# 3. Convert Dt_Customer to datetime
data["Dt_Customer"] = pd.to_datetime(data["Dt_Customer"], errors="coerce", dayfirst=True) # errors = "coerce" : If a value is invalid → replace it with NaT
#Take the column Dt_Customer, convert it to real date format,  dayfirst=True: Day-Month-Year

# Drop rows that contain missing values, Nat
data = data.dropna(subset=["Dt_Customer"]) #Ignore other columns.

# =========================
# B) FEATURE TRANSFORMATION
# =========================

# 1. Encode categorical columns , Each category gets a number.
label_encoder_education = LabelEncoder()
label_encoder_marital = LabelEncoder()

data["Education_Original"] = data["Education"] # so that the insights output are not 0,1,2 not human readable

data["Education"] = label_encoder_education.fit_transform(data["Education"])
data["Marital_Status"] = label_encoder_marital.fit_transform(data["Marital_Status"])

# 2. Create customer age
data["Age"] = 2026 - data["Year_Birth"]

# 3. Create total spending , Feature Aggregation
data["Total_Spending"] = (
    data["MntWines"] +
    data["MntFruits"] +
    data["MntMeatProducts"] +
    data["MntFishProducts"] +
    data["MntSweetProducts"] +
    data["MntGoldProds"]
)

# =========================
# C) DISCRETIZATION #Convert continuous numbers into categories.
# =========================

# Bin Income (continuous) into categories
data["Income_Bin"] = pd.cut( #Divide income into 3 ranges.
    data["Income"],
    bins=3,
    labels=["Low", "Medium", "High"]
)

# Encode Income_Bin
data["Income_Bin"] = LabelEncoder().fit_transform(data["Income_Bin"])

# =========================
# D) SCALING #Make numbers comparable in size.
# =========================

numeric_cols = ["Income", "Recency", "Age", "Total_Spending"]

scaler = StandardScaler()  # Mean = 0, Standard Deviation = 1

# Do NOT overwrite original columns
scaled_values = scaler.fit_transform(data[numeric_cols])

# Save scaled values in NEW columns
data["Income_scaled"] = scaled_values[:, 0]
data["Recency_scaled"] = scaled_values[:, 1]
data["Age_scaled"] = scaled_values[:, 2]
data["Total_Spending_scaled"] = scaled_values[:, 3]

# =========================
# E) DIMENSIONALITY REDUCTION
# =========================

# Use the SCALED columns for PCA
features_for_pca = data[["Income_scaled", "Recency_scaled", "Age_scaled", "Total_Spending_scaled"]]

pca = PCA(n_components=2)  # Create PCA Object
pca_result = pca.fit_transform(features_for_pca)  # Apply PCA

data["PCA1"] = pca_result[:, 0]
data["PCA2"] = pca_result[:, 1]

# Save preprocessed dataset
data.to_csv("data_preprocessed.csv", index=False)

print("Preprocessing completed. Saved as data_preprocessed.csv")
print("New shape:", data.shape)

# Call next step
subprocess.run(["python", "analytics.py", "data_preprocessed.csv"])