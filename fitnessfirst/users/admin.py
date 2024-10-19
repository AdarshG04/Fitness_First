from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin','is_staff', 'is_active',)
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields=('id', 'date_joined', 'last_login')
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ('is_staff', 'is_active')
    list_editable = ('is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )


admin.site.register(User, CustomUserAdmin)