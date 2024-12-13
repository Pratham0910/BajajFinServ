import json

file_path = 'DataEngineeringQ2.json'
with open(file_path, 'r') as f:
    data = json.load(f)

def is_valid_indian_phone_number(phone_number):
    if phone_number.startswith('+91'):
        phone_number = phone_number[3:]
    elif phone_number.startswith('91'):
        phone_number = phone_number[2:]
    
    if len(phone_number) != 10 or not phone_number.isdigit():
        return False
    
    return phone_number[0] in '6789'

for record in data:
    phone_number = record.get('phoneNumber', '').strip()
    record['isValidMobile'] = is_valid_indian_phone_number(phone_number)

validCount = 0
for record in data:
    if record['isValidMobile']:
        validCount += 1

print(validCount)