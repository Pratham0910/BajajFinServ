from collections import Counter
import json

file_path = 'DataEngineeringQ2.json'
with open(file_path, 'r') as f:
    data = json.load(f)

genders = [entry.get("patientDetails", {}).get("gender", "") for entry in data]

gender_counts = Counter(gender for gender in genders if gender)
mode_gender = gender_counts.most_common(1)[0][0] if gender_counts else None

imputed_genders = [gender if gender else mode_gender for gender in genders]

total_entries = len(imputed_genders)
female_count = imputed_genders.count("F")
female_percentage = round((female_count / total_entries) * 100, 2)

print(female_percentage)
