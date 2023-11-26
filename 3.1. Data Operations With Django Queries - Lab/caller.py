import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import Student


def add_students() -> None:
    Student.objects.create(
        student_id="FC5204",
        first_name="John",
        last_name="Doe",
        birth_date="1995-05-15",
        email="john.doe@university.com",
    )

    student2 = Student(
        student_id="FE0054",
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@university.com"
    )
    student2.save()

    Student.objects.create(
        student_id="FH2014",
        first_name="Alice",
        last_name="Johnson",
        birth_date="1998-02-10",
        email="alice.johnson@university.com",
    )

    Student.objects.create(
        student_id="FH2015",
        first_name="Bob",
        last_name="Wilson",
        birth_date="1996-11-25",
        email="bob.wilson@university.com",
    )


# add_students()
# print(Student.objects.all())


def get_students_info():
    result = ""

    students = Student.objects.all()

    for s in students:
        result += f"Student №{s.student_id}: {s.first_name} {s.last_name}; Email: {s.email}\n"

    return result.rstrip()


# print(get_students_info())


def update_students_emails():
    students = Student.objects.all()

    for student in students:
        new_email = student.email.replace("university.com", "uni-students.com")

        student.email = new_email
        student.save()


update_students_emails()


def truncate_students():
    all_students = Student.objects.all()
    all_students.delete()


truncate_students()
print(Student.objects.all())
print(f"Number of students: {Student.objects.count()}")