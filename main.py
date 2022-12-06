def course_name():
    """Returns the Course Name From the User Input"""
    course = input("Please enter the name of your course (e.g., CIS-434): ").upper()
    return course


def number_of_students(course):
    """Takes Course Number and Returns Number of Students in this Course"""
    num_students = input(f"Please enter the number of students in {course}: ")
    return num_students


def add_grades(students_number):
    """Takes the Number of Students in the Course and Prints Student ID, Final score, and Letter Grade"""
    for i in range(students_number):
        print(f"--- Student {i+1} ---")
        student_id = input("Enter student's ID: ")
        assignment_grade = int(input("Enter assignment's grade(0-20): "))
        while assignment_grade not in range(1, 21):
            assignment_grade = int(input("Enter a number between 0 and 20 only: "))
        term_project_grade = int(input("Enter the term project grade(0-20): "))
        while term_project_grade not in range(1, 21):
            term_project_grade = int(input("Enter a number between 0 and 20 only: "))
        quizzes_grade = int(input("Enter the quizzes' grade(0-15): "))
        while quizzes_grade not in range(1, 16):
            quizzes_grade = int(input("Enter a number between 0 and 15 only: "))
        midterm_grade = int(input("Enter the midterm grade(0-20): "))
        while midterm_grade not in range(1, 21):
            midterm_grade = int(input("Enter a number between 0 and 20 only: "))
        final_grade = int(input("Enter the final grade(0-25): "))
        while final_grade not in range(1, 26):
            final_grade = int(input("Enter a number between 0 and 25 only: "))
        # calculate the final score
        final_score = assignment_grade + term_project_grade + quizzes_grade + midterm_grade + final_grade
        # use the final score to calculate the equivalent grade letter
        grade_letter = get_grade_symbol(final_score)

        print("**********")
        print(f"    Student ID: {student_id}")
        print(f"    Final Score: {final_score}   Grade: {grade_letter}")
        print("    Has been added to the system successfully!")
        print("**********\n")


def get_grade_symbol(final_score):
    """Takes Final Score and Returns the Corresponding Letter Grade"""
    if final_score >= 93:
        grade_symbol = "A"
    elif 87 <= final_score < 93:
        grade_symbol = "A-"
    elif 83 <= final_score < 87:
        grade_symbol = "B+"
    elif 80 <= final_score < 83:
        grade_symbol = "B"
    elif 75 <= final_score < 80:
        grade_symbol = "B-"
    elif 70 <= final_score < 75:
        grade_symbol = "C+"
    elif 65 <= final_score < 70:
        grade_symbol = "C"
    elif 60 <= final_score < 65:
        grade_symbol = "D"
    elif 60 > final_score:
        grade_symbol = "F"
    return grade_symbol


def add_absences(students_number):
    """Takes the Number of Students in the Course and Prints Student ID, Number of Absences, and the Associated Warning"""
    for i in range(students_number):
        print(f"--- Student {i+1} ---")
        student_id = input("Enter student's ID: ")
        num_of_absences = int(input("Number of absences: "))
        while num_of_absences < 0:
            num_of_absences = int(input("Enter value equal or greater than 0: "))
        absence_status = get_absence_status(num_of_absences)
        print("**********")
        print(f"    Student ID: {student_id}")
        print(f"    No. of Absences: {num_of_absences} ({absence_status})")
        print("    Has been added to the system successfully!")
        print("**********\n")


def get_absence_status(num_of_absences):
    """Takes the Number of Absences and Returns a Warning String """
    if num_of_absences < 3:
        return "Without Warning"
    elif num_of_absences == 3 or num_of_absences == 4:
        return "First Warning"
    elif num_of_absences >= 5:
        return "Second Warning"


program_is_on = True
while program_is_on:
    print("------------------------------------------------------------------------------\n")
    print("Welcome to the Grading and Absence Management System for Students\n")
    print("------------------------------------------------------------------------------\n")
    print("Enter “Grades” for adding the grades of students\n"
          "Enter “Absences” for adding the number of absences for students\n"
          "Enter “Exit” for exiting from the system\n")

    user_input = input("* Enter your choice: ").lower()

    if user_input == "grades":
        # get the course name from the user
        course_name1 = course_name()
        print(f"Course name: {course_name1}")

        # get the number of students in the course
        num_of_students = int(number_of_students(course_name1))
        print(f"Number of students in {course_name1}: {num_of_students}")
        # add grades to the students and get the equivalent grade letter
        grade = add_grades(num_of_students)

    elif user_input == "absences":
        # get the course name from the user
        course_name2 = course_name()
        # print(f"Course name: {course_name}")

        # get the number of students in the course
        num_of_students = int(number_of_students(course_name2))
        print(f"Number of students in {course_name2}: {num_of_students}\n")
        absence = add_absences(num_of_students)

    elif user_input == "exit":
        program_is_on = False

    else:
        print("Invalid choice")
