class Patient:
    def __init__(self,patient_id,name,age,phone):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self):
        return (f'ID: {self.patient_id}'
                f'\nName: {self.name} '
                f'\nAge: {self.age}'
                f'\nPhone: {self.phone}')

    #def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "phone": self.phone

        }


class Doctor:
    def __init__(self,doctor_id, name, specialty, crm):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.crm = crm

    def __str__(self):
        return (f'ID: {self.doctor_id}'
                f'\nName: {self.name}'
                f'\nSpecialty: {self.specialty}'
                f'\nCrm: {self.crm}')

    #def to_dict(self):
        return {
            "doctor_id": self.doctor_id,
            "name": self.name,
            "specialty": self.specialty,
            "crm": self.crm

        }

class Appointment:
    def __init__(self,appoint_id, patient_id, doctor_id, date, hour, reason):
        self.appoint_id = appoint_id
        self.patient_id  = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.hour = hour
        self.reason = reason

    def __str__(self):
        return (f'Appointment ID: {self.appoint_id}'
                f'\nPatient ID: {self.patient_id}'
                f'\nDoctor ID: {self.doctor_id}'
                f'\nDate: {self.date}'
                f'\nTime: {self.hour}'
                f'\nReason: {self.reason}')

    #def to_dict(self):
        return {
            'appointment_id': self.appoint_id,
            'patient_id': self.patient_id,
            'doctor_id': self.doctor_id,
            'date': self.date,
            'time': self.hour,
            'reason': self.reason
        }