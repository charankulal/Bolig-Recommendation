from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class UserDetail(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    number_of_adults = models.PositiveIntegerField()
    number_of_children = models.PositiveIntegerField()
    is_student = models.BooleanField(default=False)
    university_address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    def clean(self):
        errors = {}

        # Required fields validation
        if not self.name:
            errors['name'] = 'Name is required.'
        if not self.address:
            errors['address'] = 'Address is required.'
        if self.age is None:
            errors['age'] = 'Age is required.'
        if self.number_of_adults is None:
            errors['number_of_adults'] = 'Number of adults is required.'
        if self.number_of_children is None:
            errors['number_of_children'] = 'Number of children is required.'

        # Age validation
        if self.age is not None and not (17 <= self.age <= 100):
            errors['age'] = 'Age must be between 17 and 100.'

        # number_of_adults validation
        if self.number_of_adults is not None and self.number_of_adults < 0:
            errors['number_of_adults'] = 'Number of adults cannot be negative.'

        # number_of_children validation
        if self.number_of_children is not None and self.number_of_children < 0:
            errors['number_of_children'] = 'Number of children cannot be negative.'

        # university_address required if is_student is True
        if self.is_student and not self.university_address:
            errors['university_address'] = 'University address is required if user is a student.'

        if errors:
            raise ValidationError(errors)

class Tenancy(models.Model):
    name = models.CharField(max_length=100)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=7, decimal_places=2, help_text="Size in square meters")
    total_rooms = models.PositiveIntegerField(help_text="Number of rooms")
    address = models.CharField(max_length=200)
    # Distances (in km or meters, depending on your choice)
    hospital_distance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, help_text="Distance to nearest hospital (km)")
    gym_distance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, help_text="Distance to nearest gym (km)")
    school_distance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, help_text="Distance to nearest school (km)")
    supermarket_distance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, help_text="Distance to nearest supermarket (km)")

    def __str__(self):
        return f"{self.name} - {self.address}"
