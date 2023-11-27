from django.contrib import admin

from . import models


# Register your models here.
class AgreementAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "created"]
    search_fields = ["first_name", "last_name"]
    list_per_page = 10


admin.site.register(models.Agreement, AgreementAdmin)
