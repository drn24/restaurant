from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    ordering = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"



class Item(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.TextField(max_length=256, default="", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    ordering = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.name}"

