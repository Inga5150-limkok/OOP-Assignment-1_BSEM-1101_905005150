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