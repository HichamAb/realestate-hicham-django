from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Profile

class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    
    list_display = ('first_name','last_name','email','mobile','is_staff', 'is_active',)
    list_filter = ('is_superuser',)


    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'mobile','password')}),
    
        ("Access Type", {'fields':('is_staff', 'is_superuser','is_admin')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'mobile')}),
        ('Password' ,{'fields':('password1','password2')}),
        ("Access Type", {'fields':('is_staff', 'is_superuser','is_admin')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'first_name', 'mobile')
    ordering = ('email',)
    filter_horizontal = ()
class ProfileAdmin(admin.ModelAdmin) : 
    list_display  = ('user','date_of_birth','gender','image')

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Profile,ProfileAdmin)