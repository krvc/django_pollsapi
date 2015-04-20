from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    owner = models.ForeignKey('auth.User', related_name='poll')

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choice')
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
