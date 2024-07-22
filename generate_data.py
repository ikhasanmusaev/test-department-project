import os
import django
import random
from faker import Faker
from faker.providers import job

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from employees.models import Department, Employee

fake = Faker()
fake.add_provider(job)


def create_departments(levels: int, departments_per_level: int) -> list:
    departments = []
    for i in range(levels):
        for j in range(departments_per_level):
            name = 'Department_' + str(i + 1) + '.' + str(j + 1)
            parent = None if i == 0 else random.choice(
                [d for d in departments if d.parent is None or d.parent.parent is None])
            dept = Department.objects.create(name=name, parent=parent)
            departments.append(dept)
    return departments


def generate_employees(_departments: list, num_employees: int) -> None:
    for _ in range(num_employees):
        full_name = fake.name()
        position = fake.job()
        hire_date = fake.date_between(start_date='-5y', end_date='today')
        salary = round(random.uniform(30000, 150000), 2)
        department = random.choice(_departments)

        Employee.objects.create(
            full_name=full_name,
            position=position,
            hire_date=hire_date,
            salary=salary,
            department=department
        )


if __name__ == '__main__':
    print("Starting generate...")

    print("Creating departments...")
    departments = create_departments(5, 5)
    print("End.")

    print("Generating employees...")
    generate_employees(departments, 50001)
    print("End.")

    print("Done.")