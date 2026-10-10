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
