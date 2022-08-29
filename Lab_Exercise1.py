"""
Application file:               Lab_Exercise1.py
Author/Programmer:              Ann Fernando
Application Created Date:       13th January 2022
Description:                    This application calculates the cumulative GPA (in percentage) of three course units
                                of a student.
                                Input parameters are Course title, Course code, Course credit hours and Course grade.
                                The standard formulae is used for the calculation of Overall Cumulative GPA of the
                                three subjects.
                                The result is printed in two decimal digits.
"""


def main():
    """
    Function Name:          main()
    Author/Programmer:      Ann Fernando
    Date of implementation: 13th January 2022

    No input parameters are passed for the main function and no output is returned
    :return:                None

    Description:            This function calculates the cumulative GPA of three course units.
                            User is asked to input the following for 3 course units separately:
                            1. Course title
                            2. Course code
                            3. Course credit hours
                            4. Course grade/marks
    """
    heading = "%120s\n%120s\n\n" % ("Ann Fernando", "N01517411")
    print(heading)
    print(__doc__)
    print(main.__doc__)

    first_title = input("Enter course title for first course unit:\t")
    first_code = input("Enter course code for first course unit:\t")
    first_hours = input("Enter course credit hours for first course unit:\t")
    first_grade = input("Enter course grade for first course unit:\t")

    second_title = input("\nEnter course title for second course unit:\t")
    second_code = input("Enter course code for second course unit:\t")
    second_hours = input("Enter course credit hours for second course unit:\t")
    second_grade = input("Enter course grade for second course unit:\t")

    third_title = input("\nEnter course title for third course unit:\t")
    third_code = input("Enter course code for third course unit:\t")
    third_hours = input("Enter course credit hours for third course unit:\t")
    third_grade = input("Enter course grade for third course unit:\t")

    total_credit_hours = float(first_hours) + float(second_hours) + float(third_hours)
    cumulative_gpa = ((float(first_hours) * float(first_grade)) + (float(second_hours) * float(second_grade))
                      + (float(third_hours) * float(third_grade))) / total_credit_hours

    heading += "%30s%30s%30s%30s\n\n%30s%30s%30s%30s\n%30s%30s%30s%30s\n%30s%30s%30s%30s\n%90s%30s\n\n%90s%30s\n" \
               % ("Course Title", "Course Code", "Course Credits", "Course Grade",
                  first_title, first_code, first_hours, str("%.2f" % (float(first_grade))),
                  second_title, second_code, second_hours, str("%.2f" % (float(second_grade))),
                  third_title, third_code, third_hours, str("%.2f" % (float(third_grade))),
                  "Total Credits Earned:", str("%.0f" % (float(total_credit_hours))), "Cumulative GPA:",
                  str("%.2f" % (float(cumulative_gpa))))

    print(heading)


main()
