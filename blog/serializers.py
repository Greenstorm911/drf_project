from rest_framework import serializers
from .models import Blog


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()





def check_title(value):
    if value == 'parsa':
        raise serializers.ValidationError('parsa is not allowed')

class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    writer = serializers.CharField(validators=[check_title,])
    text = serializers.CharField()
    
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)


def check_title_for_model_serializer(data):
    if data['title'] == 'parsa':
        raise serializers.ValidationError({'tilte':'parsa is not allowed'})


class CheckTitle:
    def __call__(self, value):
        if value == 'parsa':
            raise serializers.ValidationError('parsa is not allowed')


class BlogSerializer(serializers.ModelSerializer):
    #text = serializers.CharField(write_only=True)
    class Meta:
        model =Blog
        fields = "__all__"
        # ('title', '')
        # exclude = ('the field i dont want')
        read_only_fields = ('id',)
        validators = [
            check_title_for_model_serializer
        ]
    # def validate_writer(self, value):
    #     if value == 'parsa':
    #         raise serializers.ValidationError('parsa is not allowed')
    #     else:
    #         return value
    def validate(self, attrs):
        if attrs["title"] == attrs["text"]:
            raise serializers.ValidationError("title and text should not be same")
        else:
            return attrs



    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     validated_data['user'] = request.user
    #     return Blog.objects.create(**validated_data)