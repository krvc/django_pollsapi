from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Poll, Choice


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = (
            'poll', 'choice_text', 'vote')


class PollSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(many=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Poll
        fields = (
            'question', 'created_by', 'pub_date', 'choice', 'owner')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
