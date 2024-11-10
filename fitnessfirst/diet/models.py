from django.db import models
from django.conf import settings
from metrics.models import FitnessMetric

class DietCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class DietPlan(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    category = models.ForeignKey(DietCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    calories_per_day = models.IntegerField()
    # suitable_age_group = models.CharField(max_length=50, blank=True, null=True)  # E.g. '18-25', '25-40'
    min_bmi = models.FloatField(help_text="Minimum BMI for this diet plan", default='0')
    max_bmi = models.FloatField(help_text="Maximum BMI for this diet plan", default='50')
    gender = models.CharField(max_length=1, null=True, choices=GENDER_CHOICES, help_text="Gender suitability")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



# New model that links users to diet plans
class UserDietPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    diet_plan = models.ForeignKey(DietPlan, on_delete=models.SET_NULL, null=True)
    # assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="assigned_by")
    assigned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}'s Diet Plan - {self.diet_plan.title if self.diet_plan else 'None'}"
    
    @staticmethod
    def assign_diet_plan_to_user(user):
        # Get the latest FitnessMetric for the user
        latest_metric = FitnessMetric.objects.filter(user=user).order_by('-date_calculated').first()

        if not latest_metric:
            return None  # No metrics available for the user
        
        # Query for a matching DietPlan based on BMI and gender
        diet_plan = DietPlan.objects.filter(
            min_bmi__lte=latest_metric.bmi,
            max_bmi__gte=latest_metric.bmi,
            gender=latest_metric.gender
        ).first()

        # Create or update the UserDietPlan
        if diet_plan:
            user_diet_plan, created = UserDietPlan.objects.update_or_create(
                user=user,
                defaults={'diet_plan': diet_plan}
            )
            return user_diet_plan
        return None  # No matching diet plan found