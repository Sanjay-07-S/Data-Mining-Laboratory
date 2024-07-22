import pandas as pd
from sklearn.metrics import accuracy_score

original_dataset = pd.read_csv(r'D:\STUDIES\MCA\Sem 3\Data Mining LAB\Exercise 2\original_2.csv', encoding='ISO-8859-1')
altered_dataset = pd.read_csv(r'D:\STUDIES\MCA\Sem 3\Data Mining LAB\Exercise 2\altered_2.csv', encoding='ISO-8859-1')

assert original_dataset.columns.equals(altered_dataset.columns)

missing_indices = original_dataset[~original_dataset.isin(altered_dataset).all(axis=1)].index

missing_values = original_dataset.loc[missing_indices]

total_missing = len(missing_indices)

if total_missing == 0:
    print("No missing values found.")
    accuracy = None
else:
    
    missing_in_altered = altered_dataset.loc[missing_indices]


    correctly_identified = (missing_in_altered.isna().sum(axis=1) == len(altered_dataset.columns)).sum()
    accuracy = correctly_identified / total_missing

    print(f"Total Missing Values: {total_missing}")
    print(f"Correctly Identified Missing Values: {correctly_identified}")
    print(f"Accuracy: {accuracy:.2f}")

if total_missing > 0:
    print("Missing Values:")
    print(missing_values)
