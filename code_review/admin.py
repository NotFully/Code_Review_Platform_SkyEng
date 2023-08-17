from django.contrib import admin
from .models import File, ReviewComment


class FileAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'pub_date',
    )
    search_fields = (
        'user',
        'pub_date',
    )
    list_filter = (
        'user',
        'pub_date',
    )
    empty_value_display = '-null-'


admin.site.register(File, FileAdmin)
admin.site.register(ReviewComment)
