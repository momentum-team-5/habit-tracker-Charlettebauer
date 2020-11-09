from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User, Habit, Record

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Record)
admin.site.register(Habit)