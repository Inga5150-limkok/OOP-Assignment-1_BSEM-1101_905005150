# Patient Record System

A foundational Python console application built to demonstrate **Object-Oriented Programming (OOP)** concepts, object interaction, and simple data structure management.

## ✍️ Author
- **Bai Inga tomayor Kamara**

## 📋 Features

- **Patient Management**: Create, validate, and store patient profiles (ID, Name, Age, Gender).
- **Medical Records**: Log specific patient medical visits with historical tracking (Record ID, Visit Date, Status).
- **Object Interaction**: Cross-references patient entries with visit logs directly through custom class workflows.
- **State Updates**: Dynamically update the completion status of patient records.

## 🛠️ Core OOP Concepts Demonstrated

- **Classes and Objects**: Modeled structures for `Patient`, `PatientRecord`, and `PatientRecordSystem`.
- **Instance Methods**: Object-specific functionalities like updating and displaying internal system status.
- **Class Methods**: Alternative factory methods (`create_patient`) for instantiating objects dynamically.
- **Object Interactivity**: Passing objects as parameters into other object methods to handle cross-class data verification.

## 📂 Project Structure

```text
├── patient_record_system.py  # Main Python executable script
├── README.md                 # Project documentation
└── LICENSE                   # MIT License file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher installed on your system.

### Running the Application

1. **Clone or download** the project file (`patient_record_system.py`) to your local machine.
2. Open your terminal, command prompt, or preferred IDE.
3. Navigate to the directory containing the file and run the following command:

```bash
python patient_record_system.py
```

## 🧪 Expected Output Workflow

When executed, the system initializes a built-in simulation suite that:
1. Adds three sample patients to the database.
2. Prints a structured table of all registered patients.
3. Attaches three medical logs to those patient entries.
4. Simulates a clinical interaction to print records linked specifically to a single patient ID.
5. Modifies a patient's medical status from `Active` to `Completed` using an instance state change.
