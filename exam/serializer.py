from rest_framework import serializers
from exam.models import Exam
from subject.models import Subject
from subject.serializer import SubjectSerializer


class ExamSerializer(serializers.ModelSerializer):

    subject = SubjectSerializer(many=False)

    class Meta:
        model = Exam
        fields = ('id', 'name', 'subject', 'date_created')

    def create(self, validated_data):
        request = self.context.get("request")
        name = validated_data.get("name")
        subject = request.data['subject']
        subject_instance = Subject.objects.get(pk=subject['id'])
        print('data================', subject_instance)

        # throughModel = exams.subject

        exam = Exam(name=name, subject=subject_instance)
        exam.save()

        return exam



