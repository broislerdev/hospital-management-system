import json
import time
import os
from models import Patient, Doctor, Appointment
from hospital import Hospital



print(r"""
 ███╗   ███╗ ███████╗ ██████╗  ███████╗ ██╗   ██╗ ███████╗ ████████╗ ███████╗ ███╗   ███╗
 ████╗ ████║ ██╔════╝ ██╔══██╗ ██╔════╝ ╚██╗ ██╔╝ ██╔════╝ ╚══██╔══╝ ██╔════╝ ████╗ ████║
 ██╔████╔██║ █████╗   ██║  ██║ ███████╗  ╚████╔╝  ███████╗    ██║    █████╗   ██╔████╔██║
 ██║╚██╔╝██║ ██╔══╝   ██║  ██║ ╚════██║   ╚██╔╝   ╚════██║    ██║    ██╔══╝   ██║╚██╔╝██║
 ██║ ╚═╝ ██║ ███████╗ ██████╔╝ ███████║    ██║    ███████║    ██║    ███████╗ ██║ ╚═╝ ██║
 ╚═╝     ╚═╝ ╚══════╝ ╚═════╝  ╚══════╝    ╚═╝    ╚══════╝    ╚═╝    ╚══════╝ ╚═╝     ╚═╝
""")

print("  * Welcome to MedSystem — Hospital Management CLI")
time.sleep(1)
os.system('cls')

hospital = Hospital()



def show_menu():
    print(r"""
 ███╗   ███╗ ███████╗ ██████╗  ███████╗ ██╗   ██╗ ███████╗ ████████╗ ███████╗ ███╗   ███╗
 ████╗ ████║ ██╔════╝ ██╔══██╗ ██╔════╝ ╚██╗ ██╔╝ ██╔════╝ ╚══██╔══╝ ██╔════╝ ████╗ ████║
 ██╔████╔██║ █████╗   ██║  ██║ ███████╗  ╚████╔╝  ███████╗    ██║    █████╗   ██╔████╔██║
 ██║╚██╔╝██║ ██╔══╝   ██║  ██║ ╚════██║   ╚██╔╝   ╚════██║    ██║    ██╔══╝   ██║╚██╔╝██║
 ██║ ╚═╝ ██║ ███████╗ ██████╔╝ ███████║    ██║    ███████║    ██║    ███████╗ ██║ ╚═╝ ██║
 ╚═╝     ╚═╝ ╚══════╝ ╚═════╝  ╚══════╝    ╚═╝    ╚══════╝    ╚═╝    ╚══════╝ ╚═╝     ╚═╝
""")

    print("  ┌─────────────────────────────┐")
    print("  │         MAIN MENU           │")
    print("  ├─────────────────────────────┤")
    print("  │  [1]  Patients              │")
    print("  │  [2]  Doctors               │")
    print("  │  [3]  Appointments          │")
    print("  │  [0]  Exit                  │")
    print("  └─────────────────────────────┘")


def patients_menu():
    print("  ┌─────────────────────────────────┐")
    print("  │         PATIENTS MENU           │")
    print("  ├─────────────────────────────────┤")
    print("  │  [1]  Add Patient               │")
    print("  │  [2]  Remove Patient            │")
    print("  │  [3]  Search Patient            │")
    print("  │  [4]  List Patients             │")
    print("  │  [0]  Exit                      │")
    print("  └─────────────────────────────────┘")

    while True:
        option = input("\n  Select an option: ")

        if option == '1':
            name = input('Name: ')
            age = int(input('Age: '))
            phone = input('Phone: ')
            patient = Patient(None, name, age, phone)
            hospital.add_patient(patient)
            print('Patient added!')

        elif option == '2':
            patient_id = int(input('Enter the ID to remove the patient:'))
            patient = hospital.get_patient(patient_id)
            hospital.remove_patient(patient)
            print('Patient Removed')

        elif option == '3':
            patient_id = int(input('Enter the ID to search for the patient: '))
            patient = hospital.get_patient(patient_id)
            print(patient)

        elif option == '4':
            for patient in hospital.list_patients().values():
                print(patient)

        elif option == '0':
            return

def doctors_menu():
    print("  ┌─────────────────────────────────┐")
    print("  │         DOCTORS MENU            │")
    print("  ├─────────────────────────────────┤")
    print("  │  [1]  Add Doctor                │")
    print("  │  [2]  Remove Doctor             │")
    print("  │  [3]  Search Doctor             │")
    print("  │  [4]  List Doctor               │")
    print("  │  [0]  Exit                      │")
    print("  └─────────────────────────────────┘")

    while True:
        option = input("\n  Select an option: ")

        if option == '1':
            name = input('Name: ')
            specialty = input('Specialty:')
            crm = input('CRM:')
            doctor = Doctor(None, name, specialty, crm)
            hospital.add_doctor(doctor)
            print('Doctor added!')

        elif option == '2':
            doctor_id = int(input('Enter the ID to remove the Doctor:'))
            doctor = hospital.get_doctor(doctor_id)
            hospital.remove_doctor(doctor)
            print('Doctor Removed')

        elif option == '3':
            doctor_id = int(input('Enter the ID to search for the Doctor: '))
            doctor = hospital.get_doctor(doctor_id)
            print(doctor)

        elif option == '4':
            for doctor in hospital.list_doctor().values():
                print(doctor)

        elif option == '0':
            return


def appointments_menu():
    print("  ┌─────────────────────────────────┐")
    print("  │         APPOINTMENTS MENU       │")
    print("  ├─────────────────────────────────┤")
    print("  │  [1]  Schedule                  │")
    print("  │  [2]  List by Patient           │")
    print("  │  [3]  List by Doctors           │")
    print("  │  [4]  Cancel Appointments       │")
    print("  │  [0]  Exit                      │")
    print("  └─────────────────────────────────┘")

    while True:
        option = input("\n  Select an option: ")

        if option == '1':

            for patient in hospital.list_patients().values():
                print(f'Patient List \n{patient}')
            patient_id = int(input('Select a patient by ID: '))
            hospital.get_patient(patient_id)
            for doctor in hospital.list_doctor().values():
                print(f'Doctor List \n{doctor}')
            doctor_id = int(input('Select a doctor by ID: '))
            hospital.get_doctor(doctor_id)
            date = input('Enter a date that will be available for viewing: ')
            hour = input('\n Enter the time you be available that day: ')
            reason = input('\n Reason for the appointment: ')
            appointments = Appointment(None, patient_id, doctor_id, date, hour, reason)
            hospital.add_appointment(appointments)
            print('Scheduling complete!')

        elif option == '2':
            patient_id = int(input('Enter patient ID: '))
            for appointment in hospital.list_appointment().values():
                if appointment.patient_id == patient_id:
                    print(appointment)

        elif option == '3':
            doctor_id = int(input('Enter doctor ID: '))
            for appointment in hospital.list_appointment().values():
                if appointment.doctor_id == doctor_id:
                    print(appointment)

        elif option == '4':
            for appointment in hospital.list_appointment().values():
                print(appointment)
            appointment_id = int(input('Enter appointment ID to cancel: '))
            confirm = input('Would you like to cancel the appointment? (y/n): ')
            if confirm == 'y':
                appointment = hospital.get_appointment(appointment_id)
                if appointment is None:
                    print('Appointment not found!')
                else:
                    hospital.remove_appointment(appointment)
                    print('Appointment canceled!')
            else:
                print('Cancellation aborted!')
        elif option == '0':
            return

def persist_database():
    with open('hospital_data.json', 'w') as file:
        hospital_dictionary = hospital.to_dict()
        file.write(json.dumps(hospital_dictionary, indent=2))

def load_database():
    if os.path.exists('hospital_data.json') and os.path.getsize('hospital_data.json') > 0:
        with open('hospital_data.json', 'r') as file:
            data = json.loads(file.read())
            for patient_data in data['patients']:
                patient = Patient(**patient_data)
                hospital.add_patient(patient)
            for doctor_data in data['doctors']:
                doctor = Doctor(**doctor_data)
                hospital.add_doctor(doctor)
            for appointments_data in data['appointments']:
                appointments = Appointment(**appointments_data)
                hospital.add_appointment(appointments)


if __name__ == '__main__':
    try:
        while True:
            load_database()
            show_menu()
            option = input("\n  Select an option: ")

            if option == '1':
                patients_menu()
            elif option == '2':
                doctors_menu()
            elif option == '3':
                appointments_menu()
            elif option == '0':
                print("\n  Goodbye!")
                break
            else:
                print("\n  Invalid option. Try again.")
                time.sleep(1)
                os.system('cls')
    finally:
        print("Closing the application, saving data to disk...")
        persist_database()