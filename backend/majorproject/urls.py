from majorproject import views
from django.urls import re_path as url

urlpatterns=[
    url(r'^api/upload$',views.file_upload)
]