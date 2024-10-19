from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FitnessMetricForm
from .models import FitnessMetric

@login_required
def add_fitness_metric(request):
    if request.method == 'POST':
        form = FitnessMetricForm(request.POST)
        if form.is_valid():
            fitness_metric = form.save(commit=False)
            fitness_metric.user = request.user
            fitness_metric.calculate_metrics()  # Calculate BMI, WHR, WHtR
            return redirect('metrics:fitness_metrics')  # Redirect to the metrics view
    else:
        form = FitnessMetricForm()
    
    return render(request, 'metrics/add_metric.html', {'form': form})

@login_required
def view_fitness_metrics(request):
    metrics = FitnessMetric.objects.filter(user=request.user).order_by('-date')
    return render(request, 'metrics/view_metrics.html', {'metrics': metrics})
