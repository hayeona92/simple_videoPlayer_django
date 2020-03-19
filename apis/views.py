from lecture.models import Lecture
from lecture.serializers import LectureSerializer
from rest_framework import generics

# Create your views here.

class LectureList(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class LectureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
