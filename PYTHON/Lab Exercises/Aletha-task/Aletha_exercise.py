#PBV Python exercise for Aletha 
import json
import csv
from datetime import datetime

# Read external validation config file
with open("config.json", "r") as file:
    config = json.load(file)

source_file = config["source_file"]
target_file = config["target_file"]
invalid_file = config["invalid_file"]
validation_rules = config["validations"]

# Read source file dynamically
with open(source_file, "r") as file:
    reader = csv.reader(file)
    headers = next(reader)  # To Read Header
    data = [row for row in reader]

# Validation Function
def validate_value(column, value):
    rules = validation_rules.get(column, {})

    # Required check
    if rules.get("required") and not value:
        return False

    # Type validation
    expected_type = rules.get("type")
    if expected_type:
        if expected_type == "int" and not value.isdigit():
            return False
        if expected_type == "float":
            try:
                float(value)
            except ValueError:
                return False
        if expected_type == "str" and not isinstance(value, str):
            return False

    # Allowed values
    if "filter" in rules and value not in rules["filter"]:
        return False

    # Numeric range validation
    if "min" in rules and float(value) < rules["min"]:
        return False
    if "max" in rules and float(value) > rules["max"]:
        return False

    # Date format validation
    if "format" in rules:
        try:
            datetime.strptime(value, rules["format"])
        except ValueError:
            return False

    return True

# Validate dataset and separate valid/invalid records
valid_records = []
invalid_records = []

for row in data:
    row_valid = all(validate_value(headers[i], row[i]) for i in range(len(headers)))
    if row_valid:
        valid_records.append(row)
    else:
        invalid_records.append(row)

# Copy valid records to target file
with open(target_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write column headers
    writer.writerows(valid_records)

# Copy invalid records to separate file
with open(invalid_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write column headers
    writer.writerows(invalid_records)

print("Validation complete!")
print(f"Valid records saved to: {target_file}")
print(f"Invalid records saved to: {invalid_file}")