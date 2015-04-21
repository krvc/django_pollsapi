from rest_framework import generics, permissions

from django.contrib.auth.models import User

from .models import Poll
from .serializers import PollSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class PollList(generics.ListCreateAPIView):

    """
    List all polls, or create a new poll.
    """

    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Create a Poll, Update a poll, delete a poll
    """

    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
