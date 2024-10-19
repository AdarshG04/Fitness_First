from django.db import models
from users.models import CustomUser  # Assuming you have a custom user model

class FitnessMetric(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link metrics to the user
    weight = models.FloatField(help_text="Weight in kilograms")
    height = models.FloatField(help_text="Height in centimeters")
    waist_circumference = models.FloatField(help_text="Waist circumference in centimeters")
    hip_circumference = models.FloatField(help_text="Hip circumference in centimeters", null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    # These fields will store calculated metrics
    bmi = models.FloatField(null=True, blank=True)
    whr = models.FloatField(null=True, blank=True)  # Waist-to-Hip Ratio
    whtr = models.FloatField(null=True, blank=True)  # Waist-to-Height Ratio

    def __str__(self):
        return f"{self.user.username} - {self.date}"

    # Method to calculate BMI
    def calculate_bmi(self):
        if self.height > 0:
            height_in_meters = self.height / 100
            self.bmi = self.weight / (height_in_meters * height_in_meters)

    # Method to calculate Waist-to-Hip Ratio
    def calculate_whr(self):
        if self.hip_circumference and self.hip_circumference > 0:
            self.whr = self.waist_circumference / self.hip_circumference

    # Method to calculate Waist-to-Height Ratio
    def calculate_whtr(self):
        if self.height > 0:
            self.whtr = self.waist_circumference / self.height

    # A method to calculate all metrics
    def calculate_metrics(self):
        self.calculate_bmi()
        self.calculate_whr()
        self.calculate_whtr()
        self.save()  # Save the calculated values to the database
