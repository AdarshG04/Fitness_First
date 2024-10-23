from django.contrib import admin
from .models import DietCategory, DietPlan, UserDietPlan

# Register the models in the admin
admin.site.register(DietCategory)
admin.site.register(DietPlan)

# Create a custom admin view for assigning diet plans to users
class UserDietPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'diet_plan', 'assigned_by', 'assigned_date')
    list_filter = ('diet_plan', 'assigned_by')
    search_fields = ('user__username', 'diet_plan__title')

    def save_model(self, request, obj, form, change):
        # Automatically set the 'assigned_by' field to the current admin user
        if not obj.assigned_by:
            obj.assigned_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(UserDietPlan, UserDietPlanAdmin)
