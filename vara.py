print("Welcome to Student Management System")
name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter course name: ")
print("\n--- Student Details ---")
print("Name:", name)
print("Age:", age)
print("Course:", course)
if age >= 18:
    print("Status: Adult Student")
else:
    print("Status: Minor Student")
subjects = ["Python", "Git", "Database"]
print("\nEnrolled Subjects:")
for subject in subjects:
    print("-", subject)
print("\nTotal Subjects:", len(subjects))
print("Student registration completed successfully!")