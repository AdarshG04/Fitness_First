from django.contrib import admin
from .models import FitnessMetric

@admin.register(FitnessMetric)
class FitnessMetricAdmin(admin.ModelAdmin):
    list_display = ['user','gender', 'bmi', 'whr', 'whtr', 'date_calculated']
    readonly_fields = ['bmi', 'whr', 'whtr', 'date_calculated']
    search_fields = ['user__username']
    list_filter = ['gender']
