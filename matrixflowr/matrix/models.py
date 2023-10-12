from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Matrix(models.Model):
    class Meta:
        db_table = "matrices"
        verbose_name = "matrix"
        verbose_name_plural = "matrices"

    name = models.CharField(max_length=200, blank=True, default="")
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, default="")
    vendor = models.CharField(max_length=100, blank=True, default="")
    product = models.CharField(max_length=100, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")


class Flow(models.Model):
    class Meta:
        db_table = "flows"
        verbose_name = "flow"

    name = models.CharField(max_length=200, blank=True, default="")
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, default="")
    matrix = models.ForeignKey(Matrix, on_delete=models.CASCADE)
    source = models.TextField(blank=True, default="")
    destination = models.TextField(blank=True, default="")
    is_opened = models.BooleanField(default=True, blank=True, null=False)
    is_active = models.BooleanField(default=False, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="+")


class Comment(models.Model):
    class Meta:
        db_table = "comments"
        verbose_name = "comment"

    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    matrix = models.ForeignKey(Matrix, on_delete=models.CASCADE)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
