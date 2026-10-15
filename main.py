
"""
Patient Record System
Module: Object-Oriented Programming 1

This program demonstrates the use of classes, objects, instance methods, class methods,
and interaction between objects in a patient record system.
"""
# =====================================
# CLASS 1: PATIENT
# =====================================

class Patient:

    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender

    # Instance method
    def display_info(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

    # Class method
    @classmethod
    def create_patient(cls, patient_id, name, age, gender):
        return cls(patient_id, name, age, gender)

    # Interaction between Patient and PatientRecord objects
    def display_patient_record(self, record):
        if self.patient_id == record.patient_id:
            print("Patient:", self.name)
            record.display_info()
        else:
            print("This record belongs to another patient.")


# =====================================
# CLASS 2: PATIENT RECORD
# =====================================

class PatientRecord:

    def __init__(self, record_id, patient_id, visit_date, status):
        self.record_id = record_id
        self.patient_id = patient_id
        self.visit_date = visit_date
        self.status = status

    # Instance method
    def display_info(self):
        print("Record ID:", self.record_id)
        print("Patient ID:", self.patient_id)
        print("Visit Date:", self.visit_date)
        print("Status:", self.status)

    # Instance method to update a record
    def update_record(self, new_status):
        self.status = new_status
        print("Record updated successfully.")


# =====================================
# CLASS 3: PATIENT RECORD SYSTEM
# =====================================

class PatientRecordSystem:

    def __init__(self):
        # Lists are the chosen data structure
        self.patients = []
        self.records = []

    # Add a Patient object to the patient list
    def add_patient(self, patient):
        for item in self.patients:
            if item.patient_id == patient.patient_id:
                print("Patient ID already exists.")
                return

        self.patients.append(patient)
        print("Patient added successfully.")

    # Display all Patient objects
    def display_patients(self):
        print("\n===== PATIENT LIST =====")

        for patient in self.patients:
            patient.display_info()
            print("--------------------")

        print("Total patients:", len(self.patients))

    # Search for a patient by ID
    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient

        return None

    # Add a PatientRecord object to the record list
    def add_record(self, record):
        patient = self.find_patient(record.patient_id)

        if patient is None:
            print("Patient does not exist.")
            return

        for item in self.records:
            if item.record_id == record.record_id:
                print("Record ID already exists.")
                return

        self.records.append(record)
        print("Record added successfully.")

    # Display all PatientRecord objects
    def display_records(self):
        print("\n===== PATIENT RECORDS =====")

        for record in self.records:
            record.display_info()
            print("--------------------")

        print("Total records:", len(self.records))

    # Demonstrate interaction between objects
    def display_patient_records(self, patient_id):
        patient = self.find_patient(patient_id)

        if patient is None:
            print("Patient not found.")
            return

        found = False

        for record in self.records:
            if record.patient_id == patient.patient_id:
                patient.display_patient_record(record)
                found = True

        if not found:
            print("No records found for this patient.")


# =====================================
# MAIN PROGRAM: TEST THE CLASSES
# =====================================

def main():

    # Create the system object
    system = PatientRecordSystem()

    # Create Patient objects
    patient1 = Patient("P001", "Abdul Kamara", 25, "Male")
    patient2 = Patient("P002", "Fatmata Koroma", 31, "Female")

    # Create another Patient object using the class method
    patient3 = Patient.create_patient(
        "P003", "Mohamed Conteh", 40, "Male"
    )

    # Add patients to the system
    system.add_patient(patient1)
    system.add_patient(patient2)
    system.add_patient(patient3)

    # Display the patient list
    system.display_patients()

    # Create PatientRecord objects
    record1 = PatientRecord(
        "R001", "P001", "2026-10-08", "Active"
    )

    record2 = PatientRecord(
        "R002", "P002", "2026-10-09", "Active"
    )

    record3 = PatientRecord(
        "R003", "P003", "2026-10-10", "Active"
    )

    # Add records to the system
    system.add_record(record1)
    system.add_record(record2)
    system.add_record(record3)

    # Display the record list
    system.display_records()

    # Demonstrate interaction between objects
    print("\n===== OBJECT INTERACTION =====")
    system.display_patient_records("P001")

    # Demonstrate an instance method
    print("\n===== UPDATE RECORD =====")
    record1.update_record("Completed")
    record1.display_info()

    print("\nProgram completed successfully.")


if __name__ == "__main__":
    main()
