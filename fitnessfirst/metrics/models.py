# metrics/models.py
from django.db import models
from django.conf import settings



class FitnessMetric(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    waist_circumference = models.FloatField()
    hip_circumference = models.FloatField()

    bmi = models.FloatField(blank=True, null=True, help_text="Body Mass Index")
    whr = models.FloatField(blank=True, null=True, help_text="Waist-to-Hip Ratio")
    whtr = models.FloatField(blank=True, null=True, help_text="Waist-to-Height Ratio")

    date_calculated = models.DateTimeField(auto_now_add=True)

    def calculate_bmi(self):
        # BMI = weight (kg) / height^2 (m^2)
        if self.height > 0:
            self.bmi = self.weight / (self.height ** 2)

    def calculate_whr(self):
        # WHR = waist circumference / hip circumference
        if self.hip_circumference > 0:
            self.whr = self.waist_circumference / self.hip_circumference

    def calculate_whtr(self):
        # WHtR = waist circumference (cm) / height (cm)
        if self.height > 0:
            self.whtr = self.waist_circumference / (self.height * 100)

    def save(self, *args, **kwargs):
        # Calculate all metrics before saving
        self.calculate_bmi()
        self.calculate_whr()
        self.calculate_whtr()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email}'s Metrics (BMI: {self.bmi}, WHR: {self.whr}, WHtR: {self.whtr})"
