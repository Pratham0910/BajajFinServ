from collections import Counter
import json

file_path = 'DataEngineeringQ2.json'
with open(file_path, 'r') as f:
    data = json.load(f)

medicine_counts = Counter(
    med['medicineName'] 
    for record in data 
    for med in record['consultationData'].get('medicines', [])
)

third_most_common_medicine = medicine_counts.most_common(3)[2][0]
print(third_most_common_medicine)