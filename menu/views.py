from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from menu.models import *

def menu (request):
    categories = Category.objects.all().order_by("ordering")
    return render(request, "menu/menu.html", locals())
