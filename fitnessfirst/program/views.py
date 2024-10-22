from django.shortcuts import render
from .models import MembershipPlan

def get_program(request):
    programs = MembershipPlan.objects.filter(status=True)
    context = {'program': programs}
    return render(request, "programs/programs.html", context)