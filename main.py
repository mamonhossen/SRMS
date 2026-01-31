# main.py

from student import Student  #student class imported
from record_manager import RecordManager #record_manager class imported
from utils import get_non_empty_string, get_roll, display_students #utils class imported with various function


def show_menu(): # function for showing menue
    print("""
Welcome to the Student Record Management System!
Loading student records from students.csv... Done!
          Please enter a number from following that you want:
1. Add Student
2. View Students
3. Delete/remove Student
4. Search by Name
5. Search by Email
6. Exit
""")


def main():  # main function of the programme
    manager = RecordManager() #RecordManager object creation,previous csv data will be load automatically

    while True:  # infinite loop,menu will show repeatedly
        show_menu()
        choice = input("Enter your choice: ").strip()  #.strip is a srting method that will remove after,before spaces,tab,new line after taking input from user

        try:
            if choice == "1":
                name = get_non_empty_string("Enter name: ")
                roll = get_roll("Enter roll number: ")
                email = get_non_empty_string("Enter email: ")
                department = get_non_empty_string("Enter department name: ")

                student = Student(name, roll, email, department)
                manager.add_student(student)
                print("✅ Student added successfully")

            elif choice == "2":
                display_students(manager.view_students())

            elif choice == "3":
                roll = get_roll("Enter roll number to delete: ")
                confirm = input("Are you sure? (y/n): ").lower()
                if confirm == "y":
                    manager.delete_student(roll)
                    print("🗑️ Student deleted")

            elif choice == "4":
                name = get_non_empty_string("Enter name to search: ")
                display_students(manager.search_by_name(name))

            elif choice == "5":
                email = get_non_empty_string("Enter email to search: ")
                display_students(manager.search_by_email(email))

            elif choice == "6":
                print("👋 Program exited")
                break

            else:
                print("❌ Invalid option")

        except ValueError as error:  # if input is not given correctly it will show error
            print(error)


if __name__ == "__main__":
    main()
