import json

with open('DataEngineeringQ2.json') as file:
    json_data = json.load(file)


selected_data = []
for appointment in json_data:
    fullName = appointment['patientDetails']['firstName'] + ' ' + appointment['patientDetails']['lastName']

    selected_data.append({
        'appointmentId': appointment['appointmentId'],
        'phoneNumber': appointment['phoneNumber'],
        'firstName': appointment['patientDetails']['firstName'],
        'lastName': appointment['patientDetails']['lastName'],
        'fullName': fullName,
        'gender': appointment['patientDetails'].get('gender'),
        'DOB': appointment['patientDetails'].get('birthDate'),
        'medicines': appointment['consultationData']['medicines']
    })


for item in selected_data:
    print(item)