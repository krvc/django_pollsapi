from rest_framework import generics

from django.contrib.auth.models import User

from .models import Poll
from .serializers import PollSerializer, UserSerializer


class PollList(generics.ListCreateAPIView):

    """
    List all polls, or create a new poll.
    """

    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Create a Poll, Update a poll, delete a poll
    """

    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
