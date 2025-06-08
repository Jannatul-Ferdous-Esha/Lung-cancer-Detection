import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset.csv")  # Ensure this path is correct

# Feature columns — must match field_order in view
X = data[["AGE", "CHRONIC_DISEASE", "WHEEZING", "ALCOHOL_CONSUMING", "CHEST_PAIN"]]
y = data["label"]  # Replace with the actual label column name

# Create pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train
pipeline.fit(X, y)

# Save the pipeline
joblib.dump(pipeline, "pipeline.pkl")
print("✅ Model trained and saved as pipeline.pkl")
