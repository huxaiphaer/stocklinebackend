from django.contrib import admin

from users.models import User


class UsersAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UsersAdmin)
