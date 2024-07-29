""" Take original dataset as dataset 1 and remove some data from dataset 1 and take that as dataset 2.
        now using any methods find the missing values and compare both dataset and print the accuracy
  """
import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return [row for row in reader]

original_data = read_csv('original_2.csv')
altered_data = read_csv('altered_2.csv')

original_set = set(tuple(row) for row in original_data)
altered_set = set(tuple(row) for row in altered_data)

missing_set = original_set - altered_set
missing_values = list(missing_set)

missing_count = len(missing_values)
total_count = len(original_data)
accuracy = (total_count - missing_count) / total_count

print(f"Missing rows count: {missing_count}")
print(f"Accuracy: {accuracy:.2f}")
print("Missing Values:")
for row in missing_values:
    print(row)
