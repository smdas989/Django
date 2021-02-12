from django.contrib import admin
# from .models import CustomStudentModel
# from .forms import CustomStudentDetailsForm
from django.contrib.auth.admin import UserAdmin

# class CustomStudentAdmin(UserAdmin):
#     model = CustomStudentModel
#     add_form = CustomStudentDetailsForm

#     fieldsets  = (
#       *UserAdmin.fieldsets,
#       (
#         'User role',
#         {
#             'fields': (
#               'standard',)
            
#         }
#       ) 
#       )

# admin.site.register(CustomStudentModel, CustomStudentAdmin)