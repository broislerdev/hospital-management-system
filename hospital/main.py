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
            patient_id = input('ID: ')
            name = input('Name: ')
            age = int(input('Age: '))
            cpf = input('CPF:')
            phone = input('Phone: ')
            patient = Patient(patient_id, name, age, cpf, phone)
            hospital.add_patient(patient)
            print('Patient added!')

        elif option == '2':
            patient_id = input('Enter the ID to remove the patient:')
            hospital.remove_patient(patient_id)
            print('Patient Removed')

        elif option == '3':
            patient_id = input('Enter the ID to search for the patient: ')
            hospital.get_patient(patient_id)
            print(patient)

        elif option == '4':
            pass

        elif option == '0':
            return


while True:
    show_menu()
    option = input("\n  Select an option: ")

    if option == '1':
        patients_menu()
    elif option == '2':
        pass  # menu de médicos
    elif option == '3':
        pass  # menu de consultas
    elif option == '0':
        print("\n  Goodbye!")
        break
    else:
        print("\n  Invalid option. Try again.")
        time.sleep(1)
        os.system('cls')
