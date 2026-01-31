# utils.py

def get_non_empty_string(prompt):
    """
    Ensures input is not empty and is valid string.
    """
    value = input(prompt).strip()
    if not value:
        raise ValueError("❌ Input cannot be empty")
    return value


def get_roll(prompt):
    """
    Ensures roll number is an integer.
    """
    value = input(prompt).strip()
    if not value.isdigit():
        raise ValueError("❌ Roll number must be an integer")
    return int(value)


def display_students(students):
    """
    Displays student records in formatted output.
    """
    if not students:
        print("⚠️ No student records found")
        return

    print("\n📋 STUDENT RECORDS")
    print("-" * 60)
    for i, s in enumerate(students.values(), start=1):
        print(f"{i}. Name    : {s['name']}")
        print(f"   Roll No   : {s['roll']}")
        print(f"   Email     : {s['email']}")
        print(f"   Department: {s['department']}")
        print("-" * 60)
