class Hospital:
    def __init__(self):
        self.patients_dict = {}
        self.doctor_dict = {} 
        self.appointment_dict = {}

    def add_patient(self, patient):
        patient_id = len(self.patients_dict) + 1
        patient.patient_id = patient_id
        self.patients_dict[patient_id] = patient
        
    def add_doctor(self, doctor):
        doctor_id = len(self.doctor_dict) + 1
        doctor.doctor_id = doctor_id
        self.doctor_dict[doctor_id] = doctor

    def add_appointment(self, appointment):
        appoint_id = len(self.appointment_dict) + 1
        appointment.appoint_id = appoint_id
        self.appointment_dict[appoint_id] = appointment

    def remove_patient(self, patient):
        del self.patients_dict[patient.patient_id]

    def remove_doctor(self, doctor):
        del self.doctor_dict[doctor.doctor_id]

    def remove_appointment(self, appointment):
        del self.appointment_dict[appointment.appoint_id]

    def list_patients(self):
        return self.patients_dict

    def list_doctor(self):
        return self.doctor_dict

    def list_appointment(self):
        return self.appointment_dict

    def get_patient(self, patient_id):
        return self.patients_dict.get(patient_id)

    def get_doctor(self, doctor_id):
        return self.doctor_dict.get(doctor_id)

    def get_appointment(self, appoint_id):
        return self.appointment_dict.get(appoint_id)

    def to_dict(self):
        return {
            "patients": [v.to_dict() for v in self.patients_dict.values()],
            "doctors": [v.to_dict() for v in self.doctor_dict.values()],
            "appointments": [v.to_dict() for v in self.appointment_dict.values()],
        }