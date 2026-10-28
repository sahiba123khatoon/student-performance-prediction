# Student Performance Prediction

def predict_performance(marks):
    if marks >= 80:
        return "Excellent"
    elif marks >= 60:
        return "Good"
    elif marks >= 40:
        return "Average"
    else:
        return "Needs Improvement"


print("=== Student Performance Predictor ===")

try:
    marks = float(input("Enter student's marks (0-100): "))

    if 0 <= marks <= 100:
        result = predict_performance(marks)
        print("Predicted performance:", result)
    else:
        print("Please enter marks between 0 and 100.")

except ValueError:
    print("Please enter a valid number.")
