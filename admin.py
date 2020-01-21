from django.contrib import admin
from .models import *


class ApiUserAdmin(admin.ModelAdmin):

    def name(obj):
        return ("%s" % (obj.name))
    name.short_description = 'USER'

    list_display = (name, 'email', 'status')


admin.site.register(ApiUser, ApiUserAdmin)


class ApiKeyAdmin(admin.ModelAdmin):

    def user_name(obj):
        return ("%s" % (obj.user.name))
    user_name.short_description = 'Name'

    def apikey_name(obj):
        return ("%s" % (obj.key))
    apikey_name.short_description = 'TOKEN KEY'

    list_display = (user_name, apikey_name, 'active_status')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            # display all fields as text, rather than inputs
            return ('user',)
        else:
            return []


admin.site.register(ApiKey, ApiKeyAdmin)
