import json

file_path = 'DataEngineeringQ2.json'
with open(file_path, 'r') as file:
    data = json.load(file)

columns_to_check = ["firstName", "lastName", "birthDate"]

total_entries = len(data)
missing_counts = {col: 0 for col in columns_to_check}

for entry in data:
    patient_details = entry.get("patientDetails", {})
    for col in columns_to_check:
        value = patient_details.get(col, None)
        if value is None or value == "":
            missing_counts[col] += 1

missing_percentages = {
    col: round((missing_counts[col] / total_entries) * 100, 2)
    for col in columns_to_check
}

print(missing_percentages)
