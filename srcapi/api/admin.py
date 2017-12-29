from django.contrib import admin
from  django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)
class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = ('id','email','admin','create_date','active',)
    list_filter = ('admin',)
    fieldsets = (
        (None, {
            'fields': (
                'email','password'
            )
        }),
        ('Personal info',{
            'fields':('email','avatar','cover','username','first_name','last_name','facebook_id')
        }),
        ('Permissions',{
            'fields':('admin',)
        }),
    )
    add_fieldsets = (
        (None,{
            'classes' : ('wide',),
            'fields': ('email','password1','password2')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
admin.site.register(User,UserAdmin)
admin.site.unregister(Group)
