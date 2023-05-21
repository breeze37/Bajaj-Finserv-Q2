import json
import pandas as pd

with open('DataEngineeringQ2.json', 'r') as file:
    data = json.load(file)

appointments = []
for appointment in data:
    patient_details = appointment.get('patientDetails', {})  
    appointment_data = {
        'appointmentId': appointment['appointmentId'],
        'phoneNumber': appointment['phoneNumber'],
        'firstName': patient_details.get('firstName'),
        'lastName': patient_details.get('lastName'),
        'gender': 'male' if patient_details.get('gender') == 'M' else 'female' if patient_details.get('gender') == 'F' else 'others',
        'DOB': patient_details.get('birthDate'),
        'medicines': appointment['consultationData'].get('medicines')
    }
    appointments.append(appointment_data)

df = pd.DataFrame(appointments)
df['fullName'] = df['firstName'] + ' ' + df['lastName']
    
print(df[['appointmentId', 'phoneNumber', 'firstName', 'lastName', 'gender', 'DOB', 'medicines', 'fullName']])
