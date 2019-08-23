from rest_framework import serializers
from exam.models import Exam
from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer
from subject.models import Subject
from subject.serializer import SubjectSerializer


class ExamSerializer(serializers.ModelSerializer):

    subject = SubjectSerializer(many=False)
    exercise = ExerciseSerializer(read_only=True, many=True)

    class Meta:
        model = Exam
        fields = ('id', 'name', 'subject', 'exercise', 'date_created')

    def create(self, validated_data):
        request = self.context.get("request")
        name = validated_data.get("name")
        subject = request.data['subject']
        subject_instance = Subject.objects.get(pk=subject['id'])
        exercises = request.data['exercises']
        print('data================', exercises)

        # throughModel = exams.subject

        exam = Exam(name=name, subject=subject_instance)
        exam.save()

        for exercise in exercises:
            ex_name = exercise['name']
            ex_description = exercise['description']
            exercise_instance = Exercise(name=ex_name, description=ex_description,  exam=exam, subject=subject_instance)
            exercise_instance.save()

        return exam


