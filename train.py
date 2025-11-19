import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_excel("Students_Performance_data_set.xlsx")

# Encode categorical columns
label_cols = df.select_dtypes(include=['object']).columns
encoders = {}

for col in label_cols:
    enc = LabelEncoder()
    df[col] = enc.fit_transform(df[col].astype(str))
    encoders[col] = enc

# Select target
target = "What is your current CGPA?"
X = df.drop(target, axis=1)
y = df[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"Training R² Score: {train_score:.4f}")
print(f"Testing R² Score: {test_score:.4f}")

# Save model + encoders
joblib.dump(model, "model.pkl")
joblib.dump(encoders, "encoders.pkl")

print("\nModel and encoders saved successfully!")
