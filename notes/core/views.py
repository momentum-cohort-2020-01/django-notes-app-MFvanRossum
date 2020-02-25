from django.shortcuts import render
from django.http import HttpResponse

import data 

def notes_list(request):
    notes = data.NOTES
    return render(request, 'core/notes_list.html', {'notes': notes})
