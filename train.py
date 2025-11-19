import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("merged_dataset.csv")

# Select target - using ExamScore as the primary performance indicator
target = "ExamScore"
X = df.drop([target, "FinalGrade"], axis=1)  # Drop target and FinalGrade
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

# Save model (no encoders needed as all features are already numeric)
joblib.dump(model, "model.pkl")

print("\nModel saved successfully!")
