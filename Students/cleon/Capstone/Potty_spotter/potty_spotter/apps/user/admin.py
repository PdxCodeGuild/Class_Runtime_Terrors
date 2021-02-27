from django.contrib import admin

from potty_spotter.apps.user.models import User, SysAdmin, GeneralUser


class UserAdmin(admin.ModelAdmin):
    search_fields = ["username"]


admin.site.register(User, UserAdmin)
admin.site.register(SysAdmin)
admin.site.register(GeneralUser)
