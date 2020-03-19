from django.db import models

import os
# Create your models here.

def video_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    name = filename.split('.')[0]
    return os.path.join(instance.UPLOAD_PATH,name+'.'+ext)

class Lecture(models.Model):
    UPLOAD_PATH = ''
    course_name = models.CharField(max_length=255, blank=False)
    lecturer = models.CharField(max_length=255, blank=False)
    file = models.FileField(upload_to=video_upload_to, blank=False)
    loc = str(file)

    def __str__(self):
        return self.course_name
    class Meta:
        db_table = 'dataBank_lecture'
        verbose_name = 'lecture'
        verbose_name_plural = 'lecture'
