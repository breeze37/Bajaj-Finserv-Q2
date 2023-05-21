import re
import json
with open('DataEngineeringQ2.json') as file:
    data = json.load(file)

for appointment in data:
    appointment_id = appointment.get('appointmentId')
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

    print(f"Appointment ID: {appointment_id}")
    print(f"Phone Number: {phone_number}")
    print(f"Full Name: {full_name}")
    print(f"Gender: {gender}")
    print(f"Birth Date: {birth_date}")
    print(f"Medicines: {medicines}")
    print(f"Is Valid Mobile: {is_valid_mobile}")
    print("-------------------------------------")