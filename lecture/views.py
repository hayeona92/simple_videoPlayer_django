from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import generics
from rest_framework import mixins

from .models import Lecture
from .serializers import LectureSerializer
# Create your views here.



def index(request):
    return render(request, 'index.html',)

class LectureList(ListView):
    model = Lecture
    template_name = 'lecture.html'
    context_object_name = 'LectureList'


class LectureDetail(DetailView):
    template_name = 'lectureDetail.html'
    queryset = Lecture.objects.all()
    context_object_name = 'lecture'
