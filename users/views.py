from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def all_users(request):
    return HttpResponse('Returning all users')