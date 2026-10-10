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

