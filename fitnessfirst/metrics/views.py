# metrics/views.py
from django.shortcuts import render, redirect
from .forms import FitnessMetricForm
from .models import FitnessMetric

def calculate_metrics(request):
    if request.method == 'POST':
        form = FitnessMetricForm(request.POST)
        if form.is_valid():
            metric = form.save(commit=False)
            metric.user = request.user
            metric.save()
            return redirect('metrics:results', metric_id=metric.id)
    else:
        form = FitnessMetricForm()

    return render(request, 'metrics/calculate_metrics.html', {'form': form})

def results(request, metric_id):
    metric = FitnessMetric.objects.get(id=metric_id)
    return render(request, 'metrics/results.html', {'metric': metric})

