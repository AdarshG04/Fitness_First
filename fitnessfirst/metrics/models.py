# metrics/models.py
from django.db import models
from django.conf import settings



class FitnessMetric(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    waist_circumference = models.FloatField(null=True, blank=True)
    hip_circumference = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, help_text="Select your gender")

    bmi = models.FloatField(blank=True, null=True, help_text="Body Mass Index")
    whr = models.FloatField(blank=True, null=True, help_text="Waist-to-Hip Ratio")
    whtr = models.FloatField(blank=True, null=True, help_text="Waist-to-Height Ratio")

    date_calculated = models.DateTimeField(auto_now_add=True)

    def calculate_bmi(self):
        # BMI = weight (kg) / height^2 (m^2)
        if self.weight is not None and self.height is not None and self.height > 0:
            self.bmi = self.weight / (self.height ** 2)
        else:
            self.bmi = None

    def calculate_whr(self):
        # WHR = waist circumference / hip circumference
        if self.waist_circumference is not None and self.hip_circumference is not None and self.hip_circumference > 0:
            self.whr = self.waist_circumference / self.hip_circumference
        else:
            self.whr = None

    def calculate_whtr(self):
        # WHtR = waist circumference (cm) / height (cm)
        if self.waist_circumference is not None and self.height is not None and self.height > 0:
            self.whtr = self.waist_circumference / self.height
        else:
            self.whtr = None

    def save(self, *args, **kwargs):
        # Calculate all metrics before saving
        self.calculate_bmi()
        self.calculate_whr()
        self.calculate_whtr()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email}'s Metrics (BMI: {self.bmi}, WHR: {self.whr}, WHtR: {self.whtr})"
