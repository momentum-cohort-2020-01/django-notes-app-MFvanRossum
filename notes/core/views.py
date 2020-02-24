from django.shortcuts import render
from django.http import HttpResponse

import data 

def index(request):
    notes = data.NOTES
    return render(request, 'base.html', {'notes': notes})
