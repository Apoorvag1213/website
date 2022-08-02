from django.contrib import admin
from website.models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_display=('User_name','Full_name','Email_Id','password')

admin.site.register(Signup,SignupAdmin)