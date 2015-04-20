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
            'question', 'created_by', 'pub_date', 'choice')


class UserSerializer(serializers.ModelSerializer):
    polls = \
        serializers.PrimaryKeyRelatedField(many=True,
                                           queryset=Poll.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'polls')
