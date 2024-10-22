from django.contrib import admin
from users.models import User
from program.models import MembershipPlan

@admin.register(MembershipPlan)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_title', 'price')  # Display title and price in the admin listing
    search_fields = ('program_title',)