import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
df = pd.read_excel(r"C:\Users\surya\Downloads\student_performance_dataset.xlsx")

print(df.head())

# Features and target
X = df.drop(columns=["Student_ID", "Final_Result"])
y = df["Final_Result"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Probability prediction
y_prob = model.predict_proba(X_test)[:, 1]

# Risk Classification Function
def assign_risk(prob, attendance, internal):
    if prob < 0.5 or (attendance < 60 and internal < 50):
        return "High Risk"
    elif 0.5 <= prob < 0.75 or (60 <= attendance < 75):
        return "Medium Risk"
    else:
        return "Low Risk"

risk_levels = []
for i in range(len(X_test)):
    risk = assign_risk(
        y_prob[i],
        X_test.iloc[i]["Attendance"],
        X_test.iloc[i]["Internal_Marks"]
    )
    risk_levels.append(risk)

# Decision Support Function
def decision_support(risk):

    if risk == "High Risk":
        return "Your recent academic performance shows some challenges. Try improving attendance and study daily. Seeking help from teachers or classmates can help you improve gradually."

    elif risk == "Medium Risk":
        return "Your performance is progressing well but still has room for improvement. Focus on difficult subjects and maintain regular study habits."

    else:
        return "You are maintaining strong academic performance. Continue your study strategies and support classmates by sharing knowledge."

# Generate advice
advice_list = [decision_support(risk) for risk in risk_levels]

# Final results dataframe
results = X_test.copy()

results["Actual_Result"] = y_test.values
results["Predicted_Result"] = y_pred
results["Probability_of_Pass"] = y_prob.round(2)
results["Risk_Level"] = risk_levels
results["Decision_Support"] = advice_list
results["Predicted_Label"] = results["Predicted_Result"].map({0: "Fail", 1: "Pass"})

print(results.head())
