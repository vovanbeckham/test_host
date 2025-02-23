from django.shortcuts import render

from note.models import Content

# Create your views here.




def note_index(request):
    if request.user.is_authenticated:
        contents = Content.objects.all().order_by('-pk')[:10]
    else:
        contents = Content.objects.filter(is_published=True).order_by('-pk')[:10]
    return render(request, "note/note_index.html", locals())
