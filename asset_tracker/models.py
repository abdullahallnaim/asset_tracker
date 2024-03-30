from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_out_time = models.DateTimeField()
    check_in_time = models.DateTimeField(blank=True, null=True)
    condition_when_checked_out = models.CharField(max_length=100)
    condition_when_returned = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.device} - {self.employee} - {self.check_out_time}"
