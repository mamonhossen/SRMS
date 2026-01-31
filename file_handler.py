# file_handler.py

import csv  # for reading or writting csv file
import os   # is the file exist or not


class FileHandler:
    """
    Handles loading and saving student data
    from and to a CSV file.
    """

    FILE_NAME = "students.csv"

    @staticmethod   #  call by class except object
    def load_students():
        """
        Loads students from CSV file.
        If file does not exist, returns empty dictionary.
        """
        students = {}    # make an empty dictionary

        if not os.path.exists(FileHandler.FILE_NAME):
            return students

        with open(FileHandler.FILE_NAME, "r", newline="", encoding="utf-8") as file:  # unicode transformation format 8 is used for reading/writting a file correctly by converting data into binary .open it in read mode.
            reader = csv.DictReader(file) # csf file read as dictionary
            for row in reader: # using loop for read each line of csv file
                roll = int(row["roll"])
                students[roll] = {                # keeping data in dictionary making roll as key
                    "name": row["name"],
                    "roll": roll,
                    "email": row["email"],
                    "department": row["department"]
                }
        return students

    @staticmethod   #  call by class except object
    def save_students(students):
        """
        Saves all student records into CSV file.
        Automatically called after add/delete operation.
        """
        with open(FileHandler.FILE_NAME, "w", newline="", encoding="utf-8") as file:   # open file in write mode
            fieldnames = ["name", "roll", "email", "department"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)   # writer is use for dictionary to csv file creation
            writer.writeheader()   # header is written in csv

            for student in students.values():  # each student information is written in one line in csv
                writer.writerow(student)       # each student information is written in one line in csv
