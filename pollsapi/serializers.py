from .models import Poll, Choice

from rest_framework import serializers


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = (
            'poll', 'choice_text', 'vote')


class PollSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(many=True)

    class Meta:
        model = Poll
        fields = (
            'question', 'created_by', 'pub_date', 'choice')
