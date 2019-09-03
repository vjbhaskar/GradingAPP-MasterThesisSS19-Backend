import io
from rest_framework import serializers
from print_files.models import Print_File
from user.models import User
from user.serializers import UserSerializer


class PrintFileSerializer(serializers.ModelSerializer):
    # To show users
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Print_File
        fields = ('id', 'name', 'is_submitted', 'subject', 'file_obj', 'user', 'date_created')
        read_only_fields = ('user',)
        depth = 1

    def create(self, validated_data):
        # self.initial_data to get the keys from frontend sent data
        request = self.context.get("request")

        is_submitted = validated_data.get('is_submitted', False)
        is_snippet = request.data['is_snippet']

        creator_id = validated_data.get('creator_id', "")
        user_obj = User.objects.get(pk=creator_id)
        filename = validated_data.get('name', "")
        file_obj = validated_data.get('file_obj', "")
        subject_id = self.initial_data['subject_id']
        from django.core.files import File as filex
        file_obj = filex(file_obj)
        new_file = Print_File(
            name=filename,
            is_submitted=is_submitted,
            file_obj=file_obj,
            creator_id=creator_id,
            user=user_obj,
            subject_id=subject_id
        )

        new_file.save()
        return new_file
