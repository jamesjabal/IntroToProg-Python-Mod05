# --------------------------------------------------------------------------- #
# Title: Assignment05
# Desc: Assignment demonstrates using dictionaries, JSON, & exception handling
# Change Log: (Who, When, What)
#   James Jabal,8/7/2025,Created Script. Use dictionaries & JSON module.
#   James Jabal,8/8/2025,Add exception handling
#                       ,Change FileNotFoundError -> PermissionError on writing
#                       ,Show Data: Remove message string. Use CSV string.
#   James Jabal,8/9/2025,Change PermissionError -> TypeError on writing JSON.
#   James Jabal,8/10/2025,Initialize menu_choice. Update comments for A05
#   James Jabal,8/11/2025,Loop invalid student name input. Use TextIOWrapper.
#                         Moved name input reset outside of exception handler
#   James Jabal,8/12/2025,Use constants for repeated error message strings.
#                         Remove check for file as None. TextIOWrapper in use.
#                         Add Data: Reset names after (in)valid input for multi
#                         registrations, and moved outside Exception Handler.
#                         Save Data: Change JSON indent 2 -> 4 for readability.
# --------------------------------------------------------------------------- #

import json  # For json file
import io as _io  # For file object

# Define Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"
NON_SPEC_ERROR_MESSAGE:str = "There was a non-specific error!\n"
TECH_ERROR_MESSAGE:str = "-- Technical Error Message --\n"

# Define Data Variables
student_first_name: str = ''  # Holds first name of a student entered by user.
student_last_name: str = ''  # Holds last name of a student entered by user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # One row of student data (Now a Dictionary)
students: list = []  # A table of student data
file = _io.TextIOWrapper  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.

# When the program starts, read JSON file data into a list of dictionary rows
try:  # Use Exception Handling when reading file
    file = open(FILE_NAME, "r")
    students = json.load(file)  # Extract the data from the JSON file
    file.close()
# Exception Handling
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print(TECH_ERROR_MESSAGE)
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print(NON_SPEC_ERROR_MESSAGE)
    print(TECH_ERROR_MESSAGE)
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if not file.closed: file.close()  # Ensure file is closed after error

# Present and Process the data (Main Menu Loop)
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data (Add Data)
    if menu_choice == "1":  # This will not work if it is an integer!

        while student_first_name == "" or student_last_name == "": # Input loop
            try:  # Use Error Handling

                # First Name
                while student_first_name == "":
                    student_first_name = input("Enter the student's first"
                                               " name: ")
                    if not student_first_name.isalpha():
                        student_first_name = "" # Reset invalid name input
                        raise ValueError("The first name should not contain"
                                         " numbers.")

                # Last Name
                while student_last_name == "":
                    student_last_name = input("Enter the student's last"
                                              " name: ")
                    if not student_last_name.isalpha():
                        student_last_name = "" # Reset invalid name input
                        raise ValueError("The last name should not contain"
                                         " numbers.")
                # Course Name
                course_name = input("Please enter the name of the course: ")

                # Add to a dictionary (One row in a JSON file)
                student_data = {"FirstName": student_first_name,
                                "LastName": student_last_name,
                                "CourseName": course_name}

                # Add row to list of dictionaries (JSON 2D table)
                students.append(student_data)

                # Extra print to screen (uses dictionary row data)
                print(f"You have registered {student_data["FirstName"]}",
                      f"{student_data["LastName"]} for",
                      f"{student_data["CourseName"]}.")

            # Exception Handling
            except ValueError as e:
                print(e)  # Prints the custom message
                print(TECH_ERROR_MESSAGE)
                print(e.__doc__)
                print(e.__str__())
            except Exception as e:
                print(NON_SPEC_ERROR_MESSAGE)
                print(TECH_ERROR_MESSAGE)
                print(e, e.__doc__, type(e), sep='\n')
            # After Exceptions, Loop back to Input Loop

        # After valid name input, reset name to allow multiple registrations
        student_first_name = ""
        student_last_name = ""

        continue  # Go back to Main Menu Loop

    # Present the current data (Show Data)
    elif menu_choice == "2":
        # Process data to create & show a CSV string for each row in students
        print("-"*50)
        for student in students:
            print(student["FirstName"], student["LastName"],
                  student["CourseName"], sep = ",")
        print("-"*50)

        continue

    # Save the data to a file (Save Data)
    elif menu_choice == "3":
        try:  # Use Exception Handling
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent = 4)  # Write to JSON file
            file.close()

            # Display what was written to the file using the students variable
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student["FirstName"]} {student["LastName"]}",
                      f"is enrolled in {student["CourseName"]}")

        # Exception Handling
        except TypeError as e:  # Data written might not in JSON format
            print("Please check that the data is a valid JSON format\n")
            print(TECH_ERROR_MESSAGE)
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print(NON_SPEC_ERROR_MESSAGE)
            print(TECH_ERROR_MESSAGE)
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed: file.close()  # Ensure file closed after error

        continue  # Go back to Main Menu Loop

    # Stop the loop (Exit Program)
    elif menu_choice == "4":
        break  # Break out of the loop

    else:  # Go back to Main Menu Loop for a valid choice
        print("Please only choose option 1, 2, 3, or 4")

# End of Program (Outside the Main Menu Loop)
print("Program Ended")