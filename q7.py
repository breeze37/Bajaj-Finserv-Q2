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
    medicines = appointment['consultationData']['medicines']
    no_of_medicines = len(medicines)
    no_of_active_medicines = sum(1 for medicine in medicines if medicine.get('IsActive', False))
    no_of_inactive_medicines = no_of_medicines - no_of_active_medicines

    active_medicine_names = [medicine['medicineName'] for medicine in medicines if medicine.get('IsActive', False)]
    medicine_names = ', '.join(active_medicine_names)

    selected_data.append({
        'appointmentId': appointment['appointmentId'],
        'phoneNumber': appointment['phoneNumber'],
        'firstName': appointment['patientDetails']['firstName'],
        'lastName': appointment['patientDetails']['lastName'],
        'fullName': appointment['patientDetails']['firstName'] + ' ' + appointment['patientDetails']['lastName'],
        'isValidMobile': is_valid_mobile(appointment['phoneNumber']),
        'phoneNumberHash': calculate_hash(appointment['phoneNumber']) if is_valid_mobile(appointment['phoneNumber']) else None,
        'gender': appointment['patientDetails'].get('gender'),
        'DOB': appointment.get('birthDate'),
        'Age': calculate_age(appointment.get('birthDate')),
        'medicines': medicines,
        'noOfMedicines': no_of_medicines,
        'noOfActiveMedicines': no_of_active_medicines,
        'noOfInactiveMedicines': no_of_inactive_medicines,
        'medicineNames': medicine_names
    })


for item in selected_data:
    print(item)