from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .scripts import *
from .models import *

"""
object_instance = ModelName.objects.create(field=field_val)
object_instance.save()
"""