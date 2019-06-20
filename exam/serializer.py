from rest_framework import serializers
from exam.models import Exam
from subject.serializer import SubjectSerializer

class ExamSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=False)

    class Meta:
        model = Exam
        fields = ('id', 'subject', 'time_slot1', 'time_slot2','date_created')
