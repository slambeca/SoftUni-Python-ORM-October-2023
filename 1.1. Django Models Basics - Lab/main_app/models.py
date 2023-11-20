from datetime import date

from django.db import models

CITIES = [
    ('Sofia', 'Sofia'),
    ('Plovdiv', 'Plovdiv'),
    ('Burgas', 'Burgas'),
    ('Varna', 'Varna')
]


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email_address}"


class Department(models.Model):
    code = models.CharField(max_length=4, primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True)
    employees_count = models.PositiveIntegerField("Employees Count", default=1)
    location = models.CharField(choices=CITIES, max_length=20, null=True, blank=True)
    last_edited_on = models.DateTimeField(editable=False, auto_now=True)


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    duration_in_days = models.PositiveIntegerField(blank=True, null=True, verbose_name="Duration in Days")
    estimated_hours = models.FloatField(blank=True, null=True, verbose_name="Estimated Hours")
    start_date = models.DateField(verbose_name="Start Date", blank=True, null=True, default=date.today)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_edited_on = models.DateTimeField(editable=False, auto_now=True)