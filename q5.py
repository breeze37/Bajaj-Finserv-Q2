import json
import re
import datetime
import hashlib

with open('DataEngineeringQ2.json') as file:
    data = json.load(file)

for appointment in data:
    appointment_id = appointment['appointmentId']
    phone_number = appointment['phoneNumber']
    first_name = appointment['patientDetails']['firstName']
    last_name = appointment['patientDetails']['lastName']
    gender = appointment['patientDetails'].get('gender')
    birth_date = appointment['patientDetails'].get('birthDate')
    medicines = appointment['consultationData']['medicines']

    full_name = f"{first_name} {last_name}"

    def is_valid_phone_number(number):
        number = re.sub(r'\D', '', number)
        if re.match(r'^((\+|0{0,2})91)?[6-9]\d{9}$', number):
            return True
        else:
            return False
    is_valid_mobile = is_valid_phone_number(phone_number)

    def hash_phone_number(number):
        number = re.sub(r'\D', '', number)
        if is_valid_phone_number(number):
            return hashlib.sha256(number.encode()).hexdigest()
        else:
            return None

    phone_number_hash = hash_phone_number(phone_number)

    def calculate_age(dob):
        if dob is None:
            return None
        else:
            dob = datetime.datetime.strptime(dob, "%Y-%m-%dT%H:%M:%S.%fZ")
            today = datetime.datetime.now()
            age = today.year - dob.year
            if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
                age -= 1
            return age

    age = calculate_age(birth_date)

    print(f"Appointment ID: {appointment_id}")
    print(f"Phone Number: {phone_number}")
    print(f"Full Name: {full_name}")
    print(f"Gender: {gender}")
    print(f"Birth Date: {birth_date}")
    print(f"Medicines: {medicines}")
    print(f"Is Valid Mobile: {is_valid_mobile}")
    print(f"Phone Number Hash: {phone_number_hash}")
    print(f"Age: {age}")
    print("-------------------------------------")