import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the student data
data = pd.read_csv("student_stress.csv")

# Convert text values into numbers
data["exam_pressure"] = data["exam_pressure"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

data["assignment_load"] = data["assignment_load"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

# Select input columns
X = data.drop("stress_level", axis=1)

# Select output column
y = data["stress_level"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create the machine learning model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Test the model
prediction = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, prediction)

print("Model trained successfully!")
print("Model Accuracy:", accuracy)

# Save the trained model
with open("stress_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")