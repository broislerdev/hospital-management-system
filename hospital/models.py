class Patient:
    def __init__(self,patient_id,name,age,cpf,phone):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.cpf = cpf
        self.phone = phone

    def __str__(self):
        return (f'Name: {self.name} '
                f'\nAge: {self.age}'
                f'\nCPF: {self.cpf}'
                f'\nPhone: {self.phone}')


class Doctor:
    def __init__(self,doctor_id, name, specialty, crm):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.crm = crm

    def __str__(self):
        return (f'Name: {self.name}'
                f'\nSpecialty: {self.specialty}'
                f'\nCrm: {self.crm}')

class Appointment:
    def __init__(self,appoint_id, patient_id, doctor_id, date, time, reason):
        self.appoint_id = appoint_id
        self.patient_id  = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.reason = reason

    def __str__(self):
        return (f'Date: {self.date}'
                f'\nTime: {self.time}'
                f'\nReason: {self.reason}')