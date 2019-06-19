from rest_framework import serializers
from user.models import User, UserProfile
from file.models import File


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('department','photo')


class UserSerializer(serializers.ModelSerializer):

    profile = UserProfileSerializer(required=True, many=False)
    # lab_ip = LabIpSerializer(read_only=True,many=False)

    class Meta:
        model = User
        fields = ('id', 'password', 'user_type', 'username', 'email',
        'first_name', 'last_name', 'profile','files','date_created')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('files',)

    # def __init__(self, *args, **kwargs):
    #     from lab.serializer import LabIpSerializer
    #     self.fields['lab_ip'] = LabIpSerializer(read_only=True, many=False)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        # create an obj and pass the validated data into it
        # profile.user_type = profile_data.get('user_type', profile.user_type)
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        UserProfile.objects.create(user=user, **profile_data)

        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()
        profile.department = profile_data.get('department', profile.department)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance


class FileSerializer(serializers.ModelSerializer):
    # To show users
    user = UserSerializer(read_only=True,many=False)

    class Meta:
        model = File
        fields = ('name','is_submitted', 'file_obj', 'user','creator_id','date_created','file_binary')
        read_only_fields = ('user',)

    def create(self, validated_data):
        name = validated_data.get('name', "")
        is_submitted = validated_data.get('is_submitted', False)
        file_obj =  validated_data.get('file_obj', "")
        creator_id = validated_data.get('creator_id', "")
        print('creator id============ ', creator_id)
        userObj = User.objects.get(pk=creator_id)
        print('userObj ============', userObj)
        # serializer = UserSerializer(userObj)
        request = self.context['request']
        # print(serializer)
        user = validated_data.get('user')
        file_binary = validated_data.get('file_binary', "")
        file = File(name=name, is_submitted=is_submitted, file_obj=file_obj, creator_id=creator_id, user=userObj, file_binary=file_binary)

        file.save()
        return file


