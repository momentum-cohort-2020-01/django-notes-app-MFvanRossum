from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm

def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'core/notes_list.html', {'notes': notes})

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core/notes_detail.html', {'note': note, "pk": pk})

def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes-list')
    else:
        form = NoteForm()
    return render(request, 'core/post_edit.html', {'form': form})

def note_edit(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes-list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'core/post_edit.html', {'form': form})