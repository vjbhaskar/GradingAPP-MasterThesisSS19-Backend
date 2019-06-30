from rest_framework import serializers
from user.models import User, UserProfile
from file.models import File
from user.serializers import UserSerializer

class FileSerializer(serializers.ModelSerializer):
    # To show users
    user = UserSerializer(read_only=True,many=False)
    class Meta:
        model = File
        fields = ('id', 'name', 'is_submitted', 'subject', 'file_obj', 'user', 'creator_id', 'date_created')
        read_only_fields = ('user',)
        depth = 1

    def create(self, validated_data):
         # self.initial_data to get the keys from frontend sent data
        name = validated_data.get('name',"")
        is_submitted = validated_data.get('is_submitted',False)
        file_obj =  validated_data.get('file_obj',"")
        creator_id = validated_data.get('creator_id',"")
        print('creator id============ ',creator_id,)
        userObj = User.objects.get(pk=creator_id)
        print('userObj ============',userObj)
        request = self.context['request']
        #subject = validated_data.get('subject',"")
        print("True========",validated_data,self.initial_data)
        subject_id = self.initial_data['subject_id']
        self.initial_data
        # serializer = UserSerializer(userObj)
        request = self.context['request']
        # print(serializer)
        user = validated_data.get('user')
        # file_binary = validated_data.get('file_binary',"")
        file= File(name=name,is_submitted=is_submitted,file_obj=file_obj,creator_id=creator_id,user=userObj,subject_id=subject_id)

        file.save()
        return file
