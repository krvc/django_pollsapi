from .serializers import PollSerializer
from rest_framework import generics

from .models import Poll


class PollList(generics.ListCreateAPIView):

    """
    List all polls, or create a new poll.
    """

    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Create a Poll, Update a poll, delete a poll
    """

    queryset = Poll.objects.all()
    serializer_class = PollSerializer
