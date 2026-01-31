# student.py

class Student:
    """
    Student class represents a single student entity.
    It stores student information and provides a method
    to convert the object into dictionary format.
    """

    def __init__(self, name, roll, email, department):
        self.name = name
        self.roll = roll
        self.email = email
        self.department = department

    def to_dict(self):
        """
        Converts student object to dictionary.
        This format is used for saving data to CSV file.
        """
        return {
            "name": self.name,
            "roll": self.roll,
            "email": self.email,
            "department": self.department
        }
