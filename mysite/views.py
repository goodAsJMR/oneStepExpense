from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import render
import json
from datetime import datetime, date
#序列化
from django.core import serializers
#转dict
from django.forms.models import model_to_dict

# Create your views here.

def index(request):
    return render(request, 'mysite/index.html')