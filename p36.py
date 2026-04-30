import pickle
from datetime import datetime

class InvalidMarksError(Exception):
    pass

LOG_FILE = "log.txt"
DATA_FILE = "students.dat"

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

def validate_marks(marks):
    if not (0 <= marks <= 100):
        raise InvalidMarksError("Marks must be between 0 and 100")

def add_students():
    try:
        n = int(input("How many students do you want to add? "))
        records = []
        for _ in range(n):
            roll = int(input("Roll number: "))
            name = input("Name: ")
            marks = float(input("Marks: "))
            validate_marks(marks)
            records.append({"roll": roll, "name": name, "marks": marks})

        with open(DATA_FILE, "ab") as f:
            for rec in records:
                pickle.dump(rec, f)

        log(f"Added {n} student record(s)")
        print("Records added successfully.")

    except InvalidMarksError as e:
        log(f"Error: {e}")
        print(e)
    except ValueError:
        log("Error: Invalid input")
        print("Invalid input. Please enter numeric values where required.")
    except Exception as e:
        log(f"Unexpected error while adding records: {e}")
        print("An unexpected error occurred.")

def display_students():
    try:
        with open(DATA_FILE, "rb") as f:
            print("\nAll Student Records:")
            while True:
                try:
                    rec = pickle.load(f)
                    print(rec)
                except EOFError:
                    break
        log("Displayed all student records")
    except FileNotFoundError:
        log("Error: students.dat not found")
        print("No data file found.")
    except Exception as e:
        log(f"Unexpected error while displaying: {e}")
        print("An unexpected error occurred.")

def search_student():
    try:
        roll_search = int(input("Enter roll number to search: "))
        found = False
        with open(DATA_FILE, "rb") as f:
            while True:
                try:
                    rec = pickle.load(f)
                    if rec["roll"] == roll_search:
                        print("Student found:", rec)
                        found = True
                        log(f"Searched student roll {roll_search} - found")
                        break
                except EOFError:
                    break
        if not found:
            print("Student not found.")
            log(f"Searched student roll {roll_search} - not found")
    except FileNotFoundError:
        log("Error: students.dat not found")
        print("No data file found.")
    except ValueError:
        log("Error: Invalid roll number input")
        print("Invalid roll number.")
    except Exception as e:
        log(f"Unexpected error while searching: {e}")
        print("An unexpected error occurred.")

def update_marks():
    try:
        roll_update = int(input("Enter roll number to update: "))
        new_marks = float(input("Enter new marks: "))
        validate_marks(new_marks)

        records = []
        updated = False

        try:
            with open(DATA_FILE, "rb") as f:
                while True:
                    try:
                        rec = pickle.load(f)
                        if rec["roll"] == roll_update:
                            rec["marks"] = new_marks
                            updated = True
                        records.append(rec)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("No data file found.")
            log("Error: students.dat not found during update")
            return

        with open(DATA_FILE, "wb") as f:
            for rec in records:
                pickle.dump(rec, f)

        if updated:
            print("Record updated successfully.")
            log(f"Updated marks for roll {roll_update}")
        else:
            print("Student not found.")
            log(f"Update failed: roll {roll_update} not found")

    except InvalidMarksError as e:
        log(f"Error: {e}")
        print(e)
    except ValueError:
        log("Error: Invalid input in update")
        print("Invalid input.")
    except Exception as e:
        log(f"Unexpected error while updating: {e}")
        print("An unexpected error occurred.")

# Menu
while True:
    print("\n1. Add students")
    print("2. Display all")
    print("3. Search by roll")
    print("4. Update marks")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_students()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        break
    else:
        print("Invalid choice")