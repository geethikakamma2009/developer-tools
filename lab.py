
# Student Management System

students = {}

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        students[roll] = {
            "Name": name,
            "Marks": marks
        }

        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Student Records Found")
        else:
            for roll, details in students.items():
                print("\nRoll Number:", roll)
                print("Name:", details["Name"])
                print("Marks:", details["Marks"])

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
