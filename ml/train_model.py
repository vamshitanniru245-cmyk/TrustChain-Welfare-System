import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

# Load dataset
df = pd.read_csv(
    "C:/Users/vamsh/OneDrive/Desktop/TrustChain_Training_Dataset.csv"
)

# Features used for fraud detection
features = df[['income', 'claim_count']]

# Train model
model = IsolationForest(
    contamination=0.1,
    random_state=42
)

model.fit(features)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained successfully")
print("Features:", features.columns.tolist())
print("Expected Features:", model.n_features_in_)