# Clinic Patient Manager - Version 2
# Author: Walter Omara

patients = []


def add_patient():
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")

    patient = {
        "name": name,
        "age": age
    }

    patients.append(patient)
    print("\nPatient added successfully!")


def view_patients():
    if not patients:
        print("\nNo patients recorded.")
        return

    print("\nPatient List")
    print("-" * 25)

    for index, patient in enumerate(patients, start=1):
        print(f"{index}. {patient['name']} - {patient['age']} years")


def search_patient():
    if not patients:
        print("\nNo patients recorded.")
        return

    search_name = input("Enter patient name to search: ")

    found = False

    for patient in patients:
        if patient["name"].lower() == search_name.lower():
            print("\nPatient Found")
            print("-" * 25)
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            found = True

    if not found:
        print("\nPatient not found.")


while True:
    print("\nClinic Patient Manager")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        search_patient()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
