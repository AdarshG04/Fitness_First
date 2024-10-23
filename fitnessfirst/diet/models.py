from django.db import models
from django.conf import settings

class DietCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class DietPlan(models.Model):
    category = models.ForeignKey(DietCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    calories_per_day = models.IntegerField()
    suitable_age_group = models.CharField(max_length=50, blank=True, null=True)  # E.g. '18-25', '25-40'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# New model that links users to diet plans
class UserDietPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    diet_plan = models.ForeignKey(DietPlan, on_delete=models.SET_NULL, null=True)
    assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="assigned_by")
    assigned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}'s Diet Plan - {self.diet_plan.title}"
