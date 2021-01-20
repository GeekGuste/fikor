# noinspection PyUnresolvedReferences
# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    message = "Hello word"
    return HttpResponse(message)

# Create your views here.
