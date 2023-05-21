import json
import hashlib
import datetime


with open('DataEngineeringQ2.json') as file:
    json_data = json.load(file)

def is_valid_mobile(phone_number):

    phone_number = ''.join(filter(str.isdigit, phone_number))


    if phone_number.startswith('91') or phone_number.startswith('0'):
        return len(phone_number) == 10 and 6000000000 <= int(phone_number) <= 9999999999
    elif phone_number.startswith('+91'):
        return len(phone_number) == 12 and 6000000000 <= int(phone_number[3:]) <= 9999999999
    else:
        return False


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
        'noOfInactiveMedicines': no_of_inactive_medicines
    })


for item in selected_data:
    print(item)