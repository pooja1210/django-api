from django.contrib import admin
from . models import User, ActivityPeriod
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display =['user_id']

admin.site.register(User)
admin.site.register(ActivityPeriod)

