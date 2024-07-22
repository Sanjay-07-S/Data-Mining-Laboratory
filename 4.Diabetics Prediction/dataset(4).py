import pandas as pd
import numpy as np

# Define the number of rows
num_rows = 1000

# Create a dictionary with random data for a diabetes dataset
data = {
    'PatientID': range(1, num_rows + 1),
    'Age': np.random.randint(18, 90, num_rows),
    'Gender': np.random.choice(['Male', 'Female'], num_rows),
    'BMI': np.round(np.random.uniform(18.5, 50.0, num_rows), 1),
    'BloodPressure': np.random.randint(80, 180, num_rows),
    'Glucose': np.random.randint(70, 200, num_rows),
    'Insulin': np.round(np.random.uniform(15, 276, num_rows), 1),
    'DiabetesPedigreeFunction': np.round(np.random.uniform(0.1, 2.5, num_rows), 2),
    'Outcome': np.random.choice([0, 1], num_rows)  # 0 for non-diabetic, 1 for diabetic
}

# Create a DataFrame
df_diabetes = pd.DataFrame(data)

# Save the DataFrame to a CSV file
file_path_diabetes = 'diabetes_dataset.csv'
df_diabetes.to_csv(file_path_diabetes, index=False)

file_path_diabetes
