from rest_framework import serializers
from exam.models import Exam
from subject.serializer import SubjectSerializer
from lab.serializer import Time_SlotSerializer

class ExamSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=False)
    time_slot1 = Time_SlotSerializer(many=False)
    time_slot2 = Time_SlotSerializer(many=False)

    class Meta:
        model = Exam
        fields = ('id', 'subject', 'time_slot1', 'time_slot2','date_created')
