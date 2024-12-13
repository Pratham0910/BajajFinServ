import json

file_path = 'DataEngineeringQ2.json'
with open(file_path, 'r') as f:
    data = json.load(f)

total_medicines = sum(len(record['consultationData'].get('medicines', [])) for record in data)
total_records = len(data)
average_medicines = round(total_medicines / total_records, 2)
print(average_medicines)