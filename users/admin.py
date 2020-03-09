from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Snippet, Tag

admin.site.register(User, UserAdmin)
admin.site.register(Snippet)
admin.site.register(Tag)
