"""
Patient Record System
Course: PROG211 - Object-Oriented Programming 1

Purpose:
Demonstrate object-oriented programming using a
basic patient record management system.

Privacy Notice:
Use fictional patient information only.

Limitations:
This educational program does not implement
authentication, encryption, or secure database storage.
"""

# ==========================================
# CLASS 1: PATIENT
# ==========================================

class Patient:
    def __init__(self, patient_id, name, age, gender):
        if not patient_id.strip():
            raise ValueError("Patient ID cannot be empty.")

        if not name.strip():
            raise ValueError("Patient name cannot be empty.")

        if not isinstance(age, int) or not 0 <= age <= 130:
            raise ValueError("Age must be between 0 and 130.")

        self.patient_id = patient_id.strip()
        self.name = name.strip()
        self.age = age
        self.gender = gender.strip()

    # Instance method to display patient information
    def display_info(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

    # Instance method to interact with a patient record
    def show_patient_record(self, record):
        if self.patient_id == record.patient_id:
            print("Patient:", self.name)
            print("Patient ID:", self.patient_id)
            print("Record ID:", record.record_id)
            print("Visit Date:", record.visit_date)
            print("Record Status:", record.record_status)
        else:
            print("This record does not belong to this patient.")
