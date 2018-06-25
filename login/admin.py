from django.contrib import admin
from login.models import User,Competition,UserCompetion
# Register your models here.
admin.site.register([User,Competition,UserCompetion])
