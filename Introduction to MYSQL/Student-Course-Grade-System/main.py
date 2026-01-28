from studentfunction import studentsystem
from errorhandling import int_errorhandling
def main_menu():
    while True:
        print("\n" + "=" * 40)
        print("        STUDENT GRADE SYSTEM")
        print("=" * 40)
        print("1) Add Student")
        print("2) Remove Student")
        print("3) View ALL Students")
        print("4) Add Student Grades")
        print("5) View ALL Student Grades")
        print("6) View ONE Student Grades")
        print("7) Exit")
        print("=" * 40)
        choice = int_errorhandling("Enter your choice (1-6): ")
        if choice == 1:
            studentsystem.add_student()
        elif choice == 2:
            studentsystem.remove_student()
        elif choice == 3:
            studentsystem.view_students()
        elif choice == 4:
            studentsystem.add_grades()
        elif choice == 5:
            studentsystem.view_all_grades() 
        elif choice == 6:
            studentsystem.view_specific_grades()
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-7.")


main_menu()
