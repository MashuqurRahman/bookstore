from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm,CustomUserCreationForm

CustomUserModel=get_user_model()

class CustomUserAdmin(UserAdmin):
    
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUserModel
    list_display=['email','username',]


admin.site.register(CustomUserModel,CustomUserAdmin)