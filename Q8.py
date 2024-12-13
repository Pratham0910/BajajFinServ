import pandas as pd
from scipy.stats import pearsonr
import json
from datetime import datetime

file_path = 'DataEngineeringQ2.json'
with open(file_path, 'r') as file:
    data = json.load(file)

def calculate_age(birth_date):
    if pd.isnull(birth_date):
        return None
    return datetime.now().year - pd.to_datetime(birth_date).year

ages = []
medicine_counts = []

for record in data:
    patient_details = record.get('patientDetails', {})
    birth_date = patient_details.get('birthDate')
    age = calculate_age(birth_date)
    
    medicines = record.get('consultationData', {}).get('medicines', [])
    medicine_count = len(medicines)
    
    if age is not None:
        ages.append(age)
        medicine_counts.append(medicine_count)

ages_series = pd.Series(ages)
medicine_counts_series = pd.Series(medicine_counts)

correlation, _ = pearsonr(ages_series, medicine_counts_series)
correlation_rounded = round(correlation, 2)

print(correlation_rounded)