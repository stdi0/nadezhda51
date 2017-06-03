from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import News, Activities, Projects

class SomeModelAdmin(SummernoteModelAdmin):
    pass

admin.site.register(News, SomeModelAdmin)
admin.site.register(Activities, SomeModelAdmin)
admin.site.register(Projects, SomeModelAdmin)
