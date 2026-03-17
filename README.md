# Student Performance Prediction System

## Project Overview
This project predicts student academic performance using Machine Learning.  
The system analyzes key academic factors such as attendance, internal marks, assignment scores, and class participation to predict whether a student is likely to pass or fail.

The model uses Logistic Regression and provides additional insights such as risk classification and decision support recommendations for students.

---

## Technologies Used
Python  
Pandas  
NumPy  
Scikit-learn  
Power BI  

---

## Machine Learning Model
Algorithm Used: Logistic Regression  

Model Accuracy: **85%**

The model predicts student outcomes and calculates the probability of passing using historical academic data.

---

## Risk Classification
Students are categorized into three levels based on predicted probability and academic performance:

- **High Risk** – Students who may struggle academically and require immediate support  
- **Medium Risk** – Students performing moderately but needing improvement  
- **Low Risk** – Students performing well with stable academic performance  

This classification helps teachers identify students who need academic attention.

---

## Decision Support System
The system provides personalized academic advice for students based on their risk level.

- **High Risk:** Encourages improving attendance, seeking teacher support, and focusing on daily study routines.  
- **Medium Risk:** Advises strengthening weak subjects and maintaining consistent study habits.  
- **Low Risk:** Encourages maintaining current performance and supporting peers.

This helps teachers and students take **early corrective actions** before final exams.

---

## Data Visualization Dashboard
The results of the prediction system are visualized using a **Power BI dashboard**.

The dashboard displays:

- Total number of students
- Pass and Fail predictions
- Academic risk level distribution
- Attendance vs Internal Marks analysis

This visualization helps teachers quickly understand student performance and make data-driven decisions.

---

## Project Files
- `student_prediction_model.py` – Machine learning model implementation  
- `student_performance_dataset.xlsx` – Dataset used for training and testing  
- `final_student_prediction_output.csv` – Model prediction results  
- `dashboard.png` – Power BI dashboard visualization  
- `project_presentation.pptx` – Project presentation slides  

---

## Conclusion
This project demonstrates how machine learning can assist educational institutions in identifying at-risk students early and supporting teachers in making data-driven academic decisions. The integration of predictive analytics, risk classification, and dashboard visualization provides a comprehensive academic monitoring system.
