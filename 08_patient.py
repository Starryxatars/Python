class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display_info(self):
        print(f"Patient ID       : {self.patient_id}")
        print(f"Name             : {self.name}")
        print(f"Age              : {self.age}")
        print(f"Disease          : {self.disease}")
        print(f"Consultation Fee : Rs. {self.consultation_fee:.2f}")

    def total_bill(self, medicine_charges=0, room_charges=0):
        return self.consultation_fee + medicine_charges + room_charges


patient = Patient(1, "Ravi Kumar", 45, "Fever", 500)
patient.display_info()

medicine = float(input("\nEnter medicine charges: "))
room = float(input("Enter room charges: "))
print(f"Total Bill : Rs. {patient.total_bill(medicine, room):.2f}")
