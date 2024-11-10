from django.shortcuts import render
from .models import UserDietPlan, DietPlan
from metrics.models import FitnessMetric
from django.contrib.auth.decorators import login_required

@login_required
def user_diet_plan(request):

    try:
        user_metric = FitnessMetric.objects.filter(user=request.user).latest('date_calculated')
    except FitnessMetric.DoesNotExist:
        user_metric = None

    if user_metric:
        # Find the most suitable diet plan based on BMI and gender
        suitable_diet_plan = DietPlan.objects.filter(
            min_bmi__lte=user_metric.bmi,
            max_bmi__gte=user_metric.bmi,
            gender__in=[user_metric.gender, 'A']
        ).first()

        user_diet_plan, created = UserDietPlan.objects.get_or_create(user=request.user)
        if user_diet_plan.diet_plan != suitable_diet_plan:
            user_diet_plan.diet_plan = suitable_diet_plan
            user_diet_plan.save()

    else:
        suitable_diet_plan = None

    return render(request, 'diet/user_diet_plan.html', {'diet_plan': suitable_diet_plan, 'user_metric': user_metric})