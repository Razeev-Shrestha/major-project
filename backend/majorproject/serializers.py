from dataclasses import field, fields
from rest_framework import serializers
from majorproject.models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model=File
        fields=(
       'id', 'name','file'
    )