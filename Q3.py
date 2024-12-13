from datetime import datetime
import json

file_path = 'DataEngineeringQ2.json'
with open(file_path, 'r') as f:
    data = json.load(f)

def determine_age_group(birth_date_str):
    if not birth_date_str:
        return None
    birth_date = datetime.strptime(birth_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    age = (datetime.now() - birth_date).days // 365
    if age <= 12:
        return 'Child'
    elif age <= 19:
        return 'Teen'
    elif age <= 59:
        return 'Adult'
    else:
        return 'Senior'

adult_count = sum(1 for record in data if determine_age_group(record['patientDetails'].get('birthDate')) == 'Adult')
print(adult_count)