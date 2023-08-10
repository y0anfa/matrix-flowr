from django.contrib import admin
from .models import Matrix, Flow, Comment

# Register your models here.

admin.site.register(Matrix)
admin.site.register(Flow)
admin.site.register(Comment)