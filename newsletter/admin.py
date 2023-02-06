from django.contrib import admin
from .models import SubscribedUsers

admin.site.register(SubscribedUsers)


class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')
