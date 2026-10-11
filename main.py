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

    # Class method to create a Patient object
    @classmethod
    def create_patient(cls, patient_id, name, age, gender):
        return cls(patient_id, name, age, gender)


# ==========================================
# CLASS 2: PATIENT RECORD
# ==========================================

class PatientRecord:
    VALID_STATUSES = ("Active", "Completed", "Archived")

    def __init__(self, record_id, patient_id, visit_date, record_status):
        if not record_id.strip():
            raise ValueError("Record ID cannot be empty.")

        if not patient_id.strip():
            raise ValueError("Patient ID cannot be empty.")

        if not visit_date.strip():
            raise ValueError("Visit date cannot be empty.")

        if record_status not in self.VALID_STATUSES:
            raise ValueError("Invalid record status.")

        self.record_id = record_id.strip()
        self.patient_id = patient_id.strip()
        self.visit_date = visit_date.strip()
        self.record_status = record_status

    # Instance method to display record information
    def display_info(self):
        print("Record ID:", self.record_id)
        print("Patient ID:", self.patient_id)
        print("Visit Date:", self.visit_date)
        print("Record Status:", self.record_status)

    # Instance method to update record status
    def update_record(self, new_status):
        if new_status not in self.VALID_STATUSES:
            print("Invalid status. Use Active, Completed, or Archived.")
            return

        self.record_status = new_status
        print("Record status updated successfully.")


# ==========================================
# DATA STRUCTURES
# ==========================================

patients = []
patient_records = []


# ==========================================
# FUNCTIONS TO MANAGE PATIENTS
# ==========================================

def add_patient(patient):
    for existing_patient in patients:
        if existing_patient.patient_id == patient.patient_id:
            print("Error: This patient ID already exists.")
            return

    patients.append(patient)
    print("Patient added successfully.")


def display_patients():
    print("\n===== PATIENT LIST =====")

    if not patients:
        print("No patients registered.")
        return

    for patient in patients:
        patient.display_info()
        print("-" * 25)


def find_patient(patient_id):
    for patient in patients:
        if patient.patient_id == patient_id:
            return patient

    return None


# ==========================================
# FUNCTIONS TO MANAGE PATIENT RECORDS
# ==========================================

def add_record(record):
    # Check that the patient exists
    patient = find_patient(record.patient_id)

    if patient is None:
        print("Error: Patient ID does not exist.")
        return

    # Prevent duplicate record IDs
    for existing_record in patient_records:
        if existing_record.record_id == record.record_id:
            print("Error: This record ID already exists.")
            return

    patient_records.append(record)
    print("Record added successfully.")


def display_records():
    print("\n===== PATIENT RECORDS =====")

    if not patient_records:
        print("No patient records available.")
        return

    for record in patient_records:
        record.display_info()
        print("-" * 25)


def find_record(record_id):
    for record in patient_records:
        if record.record_id == record_id:
            return record

    return None


def display_patient_record(patient_id):
    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    matching_records = [
        record for record in patient_records
        if record.patient_id == patient.patient_id
    ]

    if not matching_records:
        print("No records found for this patient.")
        return

    for record in matching_records:
        patient.show_patient_record(record)
        print("-" * 25)


# ==========================================
# SAMPLE DATA AND PROGRAM TESTS
# ==========================================

def main():
    print("===================================")
    print("      PATIENT RECORD SYSTEM")
    print("===================================")

    # Create patients using the normal constructor
    patient1 = Patient("P001", "Abdul Kamara", 25, "Male")
    patient2 = Patient("P002", "Fatmata Koroma", 31, "Female")

    # Create a patient using the class method
    patient3 = Patient.create_patient(
        "P003", "Mohamed Conteh", 40, "Male"
    )

    # Add patients to the list
    add_patient(patient1)
    add_patient(patient2)
    add_patient(patient3)

    # Display all patients
    display_patients()

    # Create patient records
    record1 = PatientRecord(
        "R001", "P001", "2026-10-08", "Active"
    )

    record2 = PatientRecord(
        "R002", "P002", "2026-10-08", "Active"
    )

    record3 = PatientRecord(
        "R003", "P003", "2026-10-08", "Active"
    )

    # Add records to the list
    add_record(record1)
    add_record(record2)
    add_record(record3)

    # Display all records
    display_records()

    # Demonstrate interaction between objects
    print("\n===== OBJECT INTERACTION =====")
    patient1.show_patient_record(record1)

    # Demonstrate a record belonging to another patient
    print("\n===== RECORD OWNERSHIP CHECK =====")
    patient1.show_patient_record(record2)

    # Display records for one patient
    print("\n===== SEARCH BY PATIENT ID =====")
    display_patient_record("P002")

    # Update a record
    print("\n===== UPDATE RECORD =====")
    record1.update_record("Completed")
    record1.display_info()

    print("\nProgram finished successfully.")

# Run the program
if __name__ == "__main__":
    main()