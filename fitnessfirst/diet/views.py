from django.shortcuts import render
from .models import UserDietPlan
from django.contrib.auth.decorators import login_required

@login_required
def user_diet_plan(request):
    diet_plan = UserDietPlan.objects.filter(user=request.user).first()
    return render(request, 'diet/user_diet_plan.html', {'diet_plan': diet_plan})