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


