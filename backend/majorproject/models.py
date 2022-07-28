from django.db import models

from djongo.storage import GridFSStorage

grid_fs_storage=GridFSStorage(collection='songs')
# Create your models here.

class File(models.Model):
    name=models.CharField(max_length=64,default='',blank=True)
    file=models.FileField(upload_to='songs', default='',storage=grid_fs_storage)