from rest_framework import generics, permissions

from django.contrib.auth.models import User

from .models import Poll, Choice
from .serializers import PollSerializer, UserSerializer, ChoiceSerializer,\
    VoteSerializer


class PollList(generics.ListCreateAPIView):

    """
    List all polls, or create a new poll.
    """

    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PollDetail(generics.RetrieveDestroyAPIView):
    """
    Create a Poll, delete a poll
    """

    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ChoiceDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve a choice, update a choice
    """

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateVote(generics.CreateAPIView):
    """
    Cast vote
    """

    serializer_class = VoteSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    """
    Create an User
    """

    authentication_classes = ()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a User
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
