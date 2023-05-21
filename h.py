import pandas as pd
import json
import re
import hashlib
import datetime


with open('DataEngineeringQ2.json') as file:
    json_data = json.load(file)


def is_valid_mobile(phone_number):

    pattern = r'^(?:\+91|91)?[6-9]\d{9}$'
    return bool(re.match(pattern, phone_number))

def calculate_age(dob):
    if dob is None:
        return None

    dob = datetime.fromisoformat(dob[:-5])
    today = datetime.now()
    age = today.year - dob.year


    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        age -= 1

    return age

def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

selected_data = []


for appointment in json_data:
    appointment_data = {
        'appointmentId': appointment['appointmentId'],
        'fullName': appointment['patientDetails']['firstName'] + ' ' + appointment['patientDetails']['lastName'],
        'phoneNumber': appointment['phoneNumber'],
        'isValidMobile': is_valid_mobile(appointment['phoneNumber']),
        'phoneNumberHash': calculate_hash(appointment['phoneNumber']) if is_valid_mobile(appointment['phoneNumber']) else None,
        'gender': appointment['patientDetails'].get('gender'),
        'DOB': appointment.get('birthDate'),
        'Age': calculate_age(appointment.get('birthDate')),
        'noOfMedicines': len(appointment['consultationData']['medicines']),
        'noOfActiveMedicines': sum(1 for medicine in appointment['consultationData']['medicines'] if medicine.get('IsActive', False)),
        'noOfInActiveMedicines': sum(1 for medicine in appointment['consultationData']['medicines'] if not medicine.get('IsActive', False)),
        'MedicineNames': ', '.join([medicine['medicineName'] for medicine in appointment['consultationData']['medicines'] if medicine.get('IsActive', False)])
    }
    selected_data.append(appointment_data)


df = pd.DataFrame(selected_data)


df.to_csv('output.csv', sep='~', index=False)