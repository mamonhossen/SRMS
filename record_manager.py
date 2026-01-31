# record_manager.py

from file_handler import FileHandler #file_handler class imported


class RecordManager:
    """
    Manages student records.
    Performs add, view, delete, and search operations.
    """

    def __init__(self):
        self.students = FileHandler.load_students()  # csv data load at starting the programme

    def add_student(self, student):
        """
        Adds a new student.
        Prevents duplicate roll numbers.
        """
        if student.roll in self.students: #duplicate roll number check
            raise ValueError("❌ Roll number already exists")

        self.students[student.roll] = student.to_dict()
        FileHandler.save_students(self.students) #csv file save

    def view_students(self):
        """
        Returns all student records.
        """
        return self.students

    def delete_student(self, roll):
        """
        Deletes a student by roll number.
        """
        if roll not in self.students:
            raise ValueError("❌ Student not found")

        del self.students[roll]
        FileHandler.save_students(self.students)

    def search_by_name(self, name):
        """
        Searches students by name (partial match).
        """
        return {
            r: s for r, s in self.students.items()
            if name.lower() in s["name"].lower()
        }

    def search_by_email(self, email):
        """
        Searches students by email (exact match).
        """
        return {
            r: s for r, s in self.students.items()
            if email.lower() == s["email"].lower()
        }
