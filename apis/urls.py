from django.contrib import admin
from django.urls import path
from .views import LectureList,LectureDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('lecture/',LectureList.as_view()),
    path('lecture/<int:pk>/', LectureDetail.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
