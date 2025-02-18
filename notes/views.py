from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes

# Create your views here.
def note_list(request):
    notes = Notes.objects.all().order_by('created_at')
    return render(request, 'note_list.html', {'notes':notes})

def note_detail(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    return render(request, 'note_details.html', {'note': note})

def add_note(request):
    if request.method =='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Notes.objects.create(title = title, content=content)
        return redirect('note_list')
    return render(request, 'note_add.html')



