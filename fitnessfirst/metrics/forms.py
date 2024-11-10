# metrics/forms.py
from django import forms
from .models import FitnessMetric

class FitnessMetricForm(forms.ModelForm):
    class Meta:
        model = FitnessMetric
        fields = ['weight', 'height', 'waist_circumference', 'hip_circumference', 'gender']
        widgets = {
            'weight': forms.NumberInput(attrs={'step': '0.01'}),
            'height': forms.NumberInput(attrs={'step': '0.01'}),
            'waist_circumference': forms.NumberInput(attrs={'step': '0.01'}),
            'hip_circumference': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'weight': 'Weight (in kg) ',
            'height': 'Height (in m) ',
            'waist_circumference': 'Waist Circumference (in cm) ',
            'hip_circumference': 'Hip Circumference (in cm) ',
            'gender': 'Gender',
        }

        def save(self, commit=True):
        # Call save method of the parent class
            instance = super().save(commit=False)
        
            # Calculate metrics
            instance.calculate_bmi()
            instance.calculate_whr()
            instance.calculate_whtr()
        
            if commit:
                instance.save()
            return instance
