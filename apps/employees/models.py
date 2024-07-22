from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    def get_children(self, include_self=True):  # По необходимости
        return ', '.join(list(self.children.all().values_list('name', flat=True)))


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=250)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
