from django import forms
from .models import FitnessMetric

class FitnessMetricForm(forms.ModelForm):
    class Meta:
        model = FitnessMetric
        fields = ['weight', 'height', 'waist_circumference', 'hip_circumference']
