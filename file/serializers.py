from rest_framework import serializers

from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer
from user.models import User
from file.models import File
from user.serializers import UserSerializer


class FileSerializer(serializers.ModelSerializer):
    # To show users
    user = UserSerializer(read_only=True, many=False)
    exercise = ExerciseSerializer(read_only=True, many=False)

    class Meta:
        model = File
        fields = ('id', 'name', 'is_submitted', 'subject', 'file_obj', 'user', 'exercise', 'creator_id', 'date_created')
        read_only_fields = ('user', 'exercise')
        depth = 1

    def create(self, validated_data):
        # self.initial_data to get the keys from frontend sent data
        request = self.context.get("request")
        name = validated_data.get('name', "")
        is_submitted = validated_data.get('is_submitted', False)
        file_obj = validated_data.get('file_obj', "")
        creator_id = validated_data.get('creator_id', "")
        print('creator id============ ', creator_id,)
        user_obj = User.objects.get(pk=creator_id)
        exercise_instance = Exercise.objects.get(pk=request.data['exercise'])
        subject_id = self.initial_data['subject_id']
        file = File(name=name, is_submitted=is_submitted, file_obj=file_obj, creator_id=creator_id, user=user_obj,
                    exercise=exercise_instance, subject_id=subject_id)

        file.save()
        return file
