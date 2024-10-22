from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin','is_staff',)
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields=('id', 'date_joined', 'last_login')
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, CustomUserAdmin)