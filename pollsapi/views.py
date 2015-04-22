from rest_framework import generics, permissions, authentication

from django.contrib.auth.models import User

from .models import Poll, Choice
from .serializers import PollSerializer, UserSerializer, ChoiceSerializer,\
    VoteSerializer


class PollList(generics.ListCreateAPIView):

    """
    List all polls, or create a new poll.
    """

    authentication_classes = (authentication.BasicAuthentication,)
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
    """
    Create a Poll, delete a poll
    """

    authentication_classes = (authentication.BasicAuthentication,)
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceDetail(generics.RetrieveUpdateAPIView):
    authentication_classes = (authentication.BasicAuthentication,)
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class CreateVote(generics.CreateAPIView):
    authentication_classes = (authentication.BasicAuthentication,)
    serializer_class = VoteSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
