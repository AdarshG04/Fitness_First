# metrics/forms.py
from django import forms
from .models import FitnessMetric

class FitnessMetricForm(forms.ModelForm):
    class Meta:
        model = FitnessMetric
        fields = ['weight', 'height', 'waist_circumference', 'hip_circumference']
        widgets = {
            'weight': forms.NumberInput(attrs={'step': '0.01'}),
            'height': forms.NumberInput(attrs={'step': '0.01'}),
            'waist_circumference': forms.NumberInput(attrs={'step': '0.01'}),
            'hip_circumference': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'weight': 'Weight (kg)',
            'height': 'Height (m)',
            'waist_circumference': 'Waist Circumference (cm)',
            'hip_circumference': 'Hip Circumference (cm)',
        }
