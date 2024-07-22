
def is_missing(value):
    return value == '' or value is None

def to_float(value):
    try:
        return float(value)
    except ValueError:
        return 0.0

def to_int(value):
    try:
        return int(value)
    except ValueError:
        return -1 


def remove_duplicates(data):
    unique_data = []
    for row in data:
        if row not in unique_data:
            unique_data.append(row)
    return unique_data

def trim_whitespace(data):
    for row in data:
        for i in range(len(row)):
            if isinstance(row[i], str):
                value = row[i]
                start = 0
                end = len(value) - 1
                while start <= end and value[start] in ' \t\n\r':
                    start += 1
                while end >= start and value[end] in ' \t\n\r':
                    end -= 1
                row[i] = value[start:end + 1]
    return data

def clean_data(data):
    header = data[0]
    data = data[1:]

    cleaned_data = []
    for row in data:
        if any(is_missing(value) for value in row):
            continue 

        row[0] = to_int(row[0])  # GameID
        row[3] = to_int(row[3])  # Year
        row[6] = to_float(row[6])  # Global_Sales

        cleaned_data.append(row)

    cleaned_data = remove_duplicates(cleaned_data)

    cleaned_data = trim_whitespace(cleaned_data)

    cleaned_data.insert(0, header)

    return cleaned_data

def read_csv_file(filename):
    data = []
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            row = []
            current_value = ''
            in_quotes = False
            for char in line:
                if char == ',' and not in_quotes:
                    row.append(current_value)
                    current_value = ''
                elif char == '"':
                    in_quotes = not in_quotes
                else:
                    current_value += char
            row.append(current_value.strip('\n'))
            data.append(row)
    return data

def write_csv_file(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        for row in data:
            line = ','.join(str(value) for value in row)
            file.write(line + '\n')

def main():
    input_filename = 'V.G sales dataset.csv'
    output_filename = 'Cleaned dataset.csv'

    data = read_csv_file(input_filename)
    cleaned_data = clean_data(data)

    write_csv_file(output_filename, cleaned_data)

    for row in cleaned_data:
        print(row)


if __name__ == "__main__":
    main()