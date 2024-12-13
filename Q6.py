import json

file_path = 'DataEngineeringQ2.json'
with open(file_path, 'r') as file:
    data = json.load(file)

active_count = 0
inactive_count = 0

for record in data:
    medicines = record.get('consultationData', {}).get('medicines', [])
    for medicine in medicines:
        if medicine.get('isActive', False):
            active_count += 1
        else:
            inactive_count += 1

total_medicines = active_count + inactive_count
active_percentage = (active_count / total_medicines) * 100 if total_medicines > 0 else 0
inactive_percentage = (inactive_count / total_medicines) * 100 if total_medicines > 0 else 0

print(round(active_percentage, 2), round(inactive_percentage, 2))