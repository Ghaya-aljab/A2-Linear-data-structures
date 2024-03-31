class Patient:
    def __init__(self, patient_id, name, age, gender, medical_history=None, current_condition=None, appointment=None):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.medical_history = medical_history if medical_history else []
        self.current_condition = current_condition if current_condition else ""
        self.appointment = appointment
        self.prescriptions = Stack()

    # Getter methods
    def get_patient_id(self):
        return self.patient_id

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_medical_history(self):
        return self.medical_history

    def get_current_condition(self):
        return self.current_condition

    def get_appointment(self):
        return self.appointment

    def get_prescriptions(self):
        return self.prescriptions

    # Setter methods
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_medical_history(self, medical_history):
        self.medical_history = medical_history

    def set_current_condition(self, current_condition):
        self.current_condition = current_condition

    def set_appointment(self, appointment):
        self.appointment = appointment

    # Other methods
    def update_medical_history(self, new_history):
        self.medical_history.append(new_history)

    def update_condition(self, new_condition):
        self.current_condition = new_condition

    def schedule_appointment(self, appointment):
        self.appointment = appointment

    def add_prescription(self, prescription):
        self.prescriptions.push(prescription)

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Doctor:
    def __init__(self, doctor_id, name, specialty, availability=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.availability = availability if availability else []

    def add_availability(self, available_time):
        self.availability.append(available_time)

    def __str__(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialty: {self.specialty}"

class Prescription:
    def __init__(self, prescription_id, medication, dosage):
        self.prescription_id = prescription_id
        self.medication = medication
        self.dosage = dosage

    def __str__(self):
        return f"Prescription ID: {self.prescription_id}, Medication: {self.medication}, Dosage: {self.dosage}"

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
