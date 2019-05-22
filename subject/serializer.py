from rest_framework import serializers
from file.models import File
from subject.models import Subject


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'
