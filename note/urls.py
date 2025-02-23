

from django.urls import path

from note import views as vs


urlpatterns = [
    path('', vs.note_index, name='note-index'),

]

